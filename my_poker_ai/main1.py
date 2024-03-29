import datetime
from itertools import count
import random
import copy

import os
dirname = os.path.dirname(__file__)
import sys
sys.path.append(dirname)

from evaluate import evaluate_poker_table

to_print = False
ranks = '23456789TJQKA'

STRATEGY_INTERVAL = 10000 #10000
PLAYERS= [0,1,2,3,4,5]
PRUNE_THRESHOLD = 2  #200
LCFR_THRESHOLD = 400
DISCOUNT_INTERVAL = 1 #10
SMALL_BLIND = 50
BIG_BLIND = 100
STARTING_STACK = 10000
C = -300  #-300000000

BETTING_ROUND_PREFLOP = 0
BETTING_ROUND_FLOP = 1
BETTING_ROUND_TURN = 2
BETTING_ROUND_RIVER = 3
BETTING_OVER = 4

ACTIONS_FIRST_RAISE_CHAR=['D','E','G']
ACTIONS_SECOND_RAISE_CHAR=['E','G']
ACTIONS_FIRST_RAISE=[1/3,1/2,1]
ACTIONS_SECOND_RAISE=[1/2,1]
ACTIONS_DIC={'D':1/3,'E':1/2,'G':1}

treeMap={}

class Node:
    def __init__(self, h=False,deck=False):
        if h==False:
            self.deck = deck[:]
            self.bettingRound = 0
            self.board = []
            self.chips = [0]
            self.pFolded = [False for i in PLAYERS]
            self.pAllin = [False for i in PLAYERS]
            self.pCards = [sorted([self.deck.pop(),self.deck.pop()], key=lambda x: (-ranks.find(x[0]),x[1])) for i in PLAYERS]
            self.currentPlayer = 2 if len(PLAYERS)>2 else 1
            self.pchips = list(map(lambda x: STARTING_STACK if x > 1 else STARTING_STACK-BIG_BLIND if x==1 else STARTING_STACK-SMALL_BLIND,PLAYERS))
            #self.pchips = list(map(lambda x: STARTING_STACK/x if x > 1 else STARTING_STACK/x-BIG_BLIND if x==1 else STARTING_STACK-SMALL_BLIND,PLAYERS))
            self.pbetCurrentRound = list(map(lambda x: 0 if x > 1 else BIG_BLIND if x==1 else SMALL_BLIND,PLAYERS))
            self.pPot = [0 for i in PLAYERS]
            self.rRaise = 0
            self.actionHistory =""
            self.pMax=2
        else:
            self.deck = h.deck[:]
            self.bettingRound = h.bettingRound
            self.board = h.board[:]
            self.chips = h.chips[:]
            self.pFolded = h.pFolded[:]
            self.pAllin = h.pAllin[:]
            self.pCards = [e[:] for e in h.pCards]  #copy.deepcopy(h.pCards)
            self.currentPlayer = h.currentPlayer
            self.pchips = h.pchips[:]
            self.pbetCurrentRound = h.pbetCurrentRound[:]
            self.pPot = h.pPot[:]
            self.rRaise=h.rRaise
            self.actionHistory = h.actionHistory[:]
            self.pMax = h.pMax
    def get_values(self):
        #print(self.deck) 
        print("bettingRound: ",self.bettingRound)
        #print(self.board) 
        print("pots: ",self.chips) 
        print("folded: ",self.pFolded) 
        print("Allin: ",self.pAllin)
        #print(self.pCards)  
        print("current player: ",self.currentPlayer) 
        print("pchips: ",self.pchips) 
        print("pbet_current_round : ",self.pbetCurrentRound)
        print("player pots : ",self.pPot)
        print("raise : ",self.rRaise)
        print("pMax turn: ",self.pMax)
        return 0
"""
define infoset structure
treeMap[infoSet] = [[regretSum],[strategy]]
"""

def getshuffledDeck():
    cardspersuit=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits=['c','d','h','s']
    deck=[]
    for suit in suits:
        deck.extend([card+suit for card in cardspersuit])
    random.shuffle(deck)
    return deck

def updateStrategy(h, p):
    #print("Updating Strategy")
    if h.bettingRound>0 or noActionleft_P(h,p) or isTerminal(h):
        return 
    elif ischanceNode(h):
        # No need to fetch next betting round
        #nextRound(h)
        #updateStrategy(h,p)
        return
    elif h.currentPlayer==p:
        #print('1')
        I = getInformationSet(h, p)
        actions=getActions(h)
        if I not in treeMap:
            initializeInfoset(I,h,len(actions))
        strategyI = calculateStrategy(I)

        index = chooseActionFromStrategy(strategyI)
        treeMap[I][1][index]=treeMap[I][1][index]+1
        doAction(h, actions[index])
        updateStrategy(h,p)
    else:
        #print('2')
        actions=getActions(h)
        for action in actions:
            _h=Node(h=h)
            doAction(_h, action)
            updateStrategy(_h,p)
    return

def discountRegrets(I,d):
    #print("check")
    assert I in treeMap, "Infoset not found"
    treeMap[I][0]=[e/d for e in treeMap[I][0]]
    if len(treeMap[I])>1:
        treeMap[I][1]=[e/d for e in treeMap[I][1]]
    return 

def isTerminal(h):
    if h.bettingRound == 4 or h.pFolded.count(True) == len(PLAYERS)-1 or (h.pFolded.count(True)+h.pAllin.count(True))==len(PLAYERS):
        return True
    if h.bettingRound==3 and ischanceNode(h)==True:
        return True
    return False

def updatechips(h):
    if to_print==True:
        print("Updating chips")
    presentPot = len(h.chips)-1
    while sum(h.pbetCurrentRound)>0.1:
        if presentPot > len(h.chips)-1:
            h.chips.append(0)   # add side pot

        minbet = min(e for i,e in enumerate(h.pbetCurrentRound) if (e > 0.1 and h.pFolded[i]!=True))  ## is near zero value
        h.chips[-1]=h.chips[-1]+sum((minbet if e-minbet>0.1 else e) for e in h.pbetCurrentRound if e > 0.1) # update pot chips
        h.pPot = [presentPot if e>0.1 else h.pPot[i] for i,e in enumerate(h.pbetCurrentRound)] # update potnumber for each player
        #pot for folded players is also updated but does not cause any harm later on 
        h.pbetCurrentRound = [e-minbet if e-minbet>.1 else 0 for i,e in enumerate(h.pbetCurrentRound)] # update current round chips left for each player
        presentPot+=1
        if presentPot>10:
            raise AssertionError ("Infinite loop possible")
    
    if to_print==True:
        h.get_values()
        print("\n")
    return

def showdown(h):
    if h.bettingRound !=4:
        updatechips(h)
    # implement hand rankings
    if h.bettingRound==BETTING_ROUND_PREFLOP:
        h.board.extend(sorted([h.deck.pop(),h.deck.pop(),h.deck.pop()],key=lambda x: (-ranks.find(x[0]),x[1])))
    elif h.bettingRound==BETTING_ROUND_FLOP:
        h.board.append(h.deck.pop())
    elif h.bettingRound==BETTING_ROUND_TURN:
        h.board.append(h.deck.pop())

    scores = evaluate_poker_table(h.pCards,h.board)
    scores_and_index=[(i,e,h.pPot[i]) for i,e in enumerate(scores)]
    players = sorted(scores_and_index , key=lambda x:(x[1],-x[2]),reverse=True)
    #print(players)
    for i in range(len(players)):
        p=players[i][0]
        if h.pFolded[p]!=True:
            eq_score=i
            count_eq=1
            for j in range(i+1,len(PLAYERS)):
                if players[i][1]!=players[j][1]:
                    break
                if h.pFolded[players[j][0]]!=True:
                    count_eq+=1
                    eq_score=j
            pot=h.pPot[p] 
            for pot_i in range(0,pot+1):
                for j in range(i,eq_score+1):
                    if h.pFolded[players[j][0]]!=True:
                        h.pchips[players[j][0]]+=h.chips[pot_i]/count_eq
                h.chips[pot_i]=0
            if pot == len(h.chips):
                break
    """
    players=PLAYERS[:]
    random.shuffle(players)
    for p in players:
        if h.pFolded[p]!=True:
            pot=h.pPot[p] 
            for i in range(0,pot+1):
                h.pchips[p]+=h.chips[i]
                h.chips[i]=0
            if pot == len(h.chips):
                break
    """
    return

def getUtility(h,p):
    assert isTerminal(h),"getUtility called for non-terminal node"
    showdown(h)
    return h.pchips[p]-STARTING_STACK

def regretifFolded(h,p):
    assert h.pFolded[p],"Player has not folded yet"
    return h.pchips[p]-STARTING_STACK

def noActionleft_P(h,p):
    _answer = h.pFolded[p] or h.pAllin[p]
    return _answer

def nextRound(h):
    if to_print==True:
        print("Getting next round")
    assert ischanceNode(h),"h is not a change node, next round can't be requested"

    h.bettingRound+=1
    h.pMax=0

    setcurrentPlayer=False
    for e in PLAYERS:
        if h.pFolded[e]!=True and h.pAllin[e]!=True:
            h.currentPlayer=e
            setcurrentPlayer=True
            break
    assert setcurrentPlayer==True, "h is a terminal node"
    h.rRaise=0
    presentPot = len(h.chips) -1
    while sum(h.pbetCurrentRound)>0:
        if presentPot > len(h.chips)-1:
            h.chips.append(0)   # add side pot
        
        minbet = min(e for i,e in enumerate(h.pbetCurrentRound) if (e > 0.1 and h.pFolded[i]!=True))  ## is near zero value
        h.chips[-1]=h.chips[-1]+sum((minbet if e-minbet>.1 else e) for e in h.pbetCurrentRound if e > 0.1) # update pot chips
        h.pPot = [presentPot if e>0.1 else h.pPot[i] for i,e in enumerate(h.pbetCurrentRound)] # update potnumber for each player
        h.pbetCurrentRound = [e-minbet if e-minbet>.1 else 0 for i,e in enumerate(h.pbetCurrentRound)] # update current round chips left for each player
        #minbet = min(e for e in h.pbetCurrentRound if e > 0)  ## is near zero value
        #h.chips[-1]=h.chips[-1]+sum(minbet for e in h.pbetCurrentRound if e > 0) # update pot chips
        #h.pPot = [presentPot if e>0 else h.pPot[i] for i,e in enumerate(h.betCurrentRound)] # update potnumber for each player
        #h.pbetCurrentRound = [e-minbet if e>0 else 0 for i,e in enumerate(h.betCurrentRound)] # update current round chips left for each player
        presentPot+=1
        if presentPot>10:
            raise AssertionError ("Infinite loop possible")
    #print(h.bettingRound,h.bettingRound==BETTING_ROUND_FLOP)
    if h.bettingRound==BETTING_ROUND_FLOP:
        h.board.extend(sorted([h.deck.pop(),h.deck.pop(),h.deck.pop()],key=lambda x: (-ranks.find(x[0]),x[1])))

    elif h.bettingRound==BETTING_ROUND_TURN:
        h.board.append(h.deck.pop())
    elif h.bettingRound==BETTING_ROUND_RIVER:
        h.board.append(h.deck.pop())
    else:
        raise AssertionError ("Next round undefined")

    
    if to_print==True:
        h.get_values()
        print("\n")
    return

def ischanceNode(h):
    bet=None
    maxbet=max(h.pbetCurrentRound)
    assert maxbet>-.1,"Negative value found"
    if maxbet<0.1:
        assert h.rRaise==0, "Raise not zero but bet is zero"
        if h.pMax>h.currentPlayer:
            return True
        else:
            return False
        """
        if h.pMax==True:
            #h.pMax=False
            print("fuck")
            return True
        else:
            if h.currentPlayer==PLAYERS[-1]:
                h.pMax=True
            print("fuck")
            return False
        """
    for i,e in enumerate(h.pbetCurrentRound):
        if h.pFolded[i]!=True and h.pAllin[i]!=True:
            if e-maxbet<-.1:
                return False
            if bet!=None:
                if abs(bet-e)>.1:
                    return False
            else:
                bet=e
    if h.bettingRound==BETTING_ROUND_PREFLOP and h.currentPlayer==1 and len(PLAYERS)>2 and h.rRaise==0:
        return False
    return True

def doAction(h,action):
    if to_print==True:
        print("Doing Action")
        print("Action: ",action)

    p=h.currentPlayer
    playerchips=h.pchips[p]
    toMatch=max(h.pbetCurrentRound)
    potSize=sum(h.chips)+sum(h.pbetCurrentRound)
    callSize=toMatch-h.pbetCurrentRound[p]

    h.actionHistory+=action

    if action in ACTIONS_DIC:
        betratio=ACTIONS_DIC[action]
        bet=betratio*potSize
        h.pchips[p]-=bet 
        h.pbetCurrentRound[p]+=bet 
        h.rRaise+=1
    elif action=='F':
        h.pFolded[p]=True
    elif action=='C':
        bet = callSize
        h.pchips[p]-=bet 
        h.pbetCurrentRound[p]+=bet 
    elif action =='A':
        h.pAllin[p]=True
        bet=playerchips
        h.pchips[p]-=bet 
        h.pbetCurrentRound[p]+=bet 
        if bet>toMatch:
            h.rRaise+=1
    else:
        raise AssertionError ("This else statement is unreachable")

    next_available_players=[]
    if p == len(PLAYERS)-1:
        next_available_players = PLAYERS[:-1]
    elif p==0:
        next_available_players.extend(PLAYERS[p+1:])
    else:
        next_available_players.extend(PLAYERS[p+1:])
        next_available_players.extend(PLAYERS[:p])

    for player in next_available_players:
        if h.pAllin[player]!=True and h.pFolded[player]!=True:
            h.currentPlayer=player
            break
    h.pMax=max(h.pMax,h.currentPlayer)
    if to_print==True:
        h.get_values()  #print node
        print("\n")
    return 
    

def getInformationSet(h,p):
    assert h.currentPlayer==p, "Infoset requested not for current player"
    actionInfoset=h.actionHistory
    cardsInfoset=h.pCards[p][0]+h.pCards[p][0][1]
    for e in h.board:
        cardsInfoset+=e
    return cardsInfoset+','+actionInfoset

def calculateStrategy(I):
    assert I in treeMap, "Infoset not found"
    regretSum=treeMap[I][0]
    #strategyI=[]
    numActions=len(regretSum)
    assert numActions>0, "Zero actions found in infoSet"
    _sum=sum(e for e in regretSum)
    #for e in regretSum:
    if _sum>0:
        strategyI = [e/_sum for e in regretSum]            ## update R+
    else:
        strategyI = [1/numActions]*numActions

    return strategyI

def chooseActionFromStrategy(strategyI):
    return random.choices(range(len(strategyI)), strategyI)[0]

def getActions(h):
    if to_print==True:
        print("Getting actions")
    #h.get_values()
    p=h.currentPlayer
    playerchips=h.pchips[p]
    toMatch=max(h.pbetCurrentRound)
    potSize=sum(h.chips)+sum(h.pbetCurrentRound)
    callSize=toMatch-h.pbetCurrentRound[p]
    #print(playerchips,toMatch,potSize,callSize)
    #assert callSize>0 or (h.bettingRound==BETTING_ROUND_PREFLOP and h.currentPlayer==1 and len(PLAYERS)>2) ,"Player call size is zero"
    actions=[]
    if h.rRaise==0:
        ACTIONS_RAISE= ACTIONS_FIRST_RAISE
        ACTIONS_RAISE_CHAR=ACTIONS_FIRST_RAISE_CHAR
    else:
        ACTIONS_RAISE=ACTIONS_SECOND_RAISE
        ACTIONS_RAISE_CHAR=ACTIONS_SECOND_RAISE_CHAR

    raiseSizes = [e*potSize for e in ACTIONS_RAISE]
    firstRaise = None
    lastRaise = None
    for i,e in enumerate(raiseSizes):
        if e>callSize+.1 and firstRaise==None:
            firstRaise=i
        if e>playerchips-.1 and lastRaise==None:
            lastRaise=i
    if lastRaise==None:
        lastRaise=len(raiseSizes)
    if firstRaise==None:
        firstRaise=len(raiseSizes)
    if lastRaise<=firstRaise:
        if callSize>playerchips-.1:
            actions.extend(['F','A'])
        else:
            actions.extend(['F','C','A'])
    else:
        actions.extend(['F','C'])
        for i in range(firstRaise,lastRaise):
            actions.append(ACTIONS_RAISE_CHAR[i])
        actions.append('A')
    if to_print==True:
        print("Actions found: ",actions,"\n")
    return actions

def getnumActions(h):
    actions=getActions(h)
    return len(actions)

def updateRegrets(I,value,_value):
    treeMap[I][0]=[(e+_value[i]-value if _value[i]!=None else e) for i,e in enumerate(treeMap[I][0])]
    return 

def initializeInfoset(I, h, numActions=None):
    if numActions == None:
        numActions = getnumActions(h)
    treeMap[I]=[[0]*numActions]
    if h.bettingRound==0:
        treeMap[I].append([0]*numActions)
    return 


def traverseMCCFR_P(h,p):
    if isTerminal(h):
        #h2 = calculateWinner(h)
        utility = getUtility(h,p)
        return utility
    elif h.pFolded[p]:
        return regretifFolded(h,p)
    elif ischanceNode(h):
        nextRound(h)
        return traverseMCCFR_P(h,p)
    elif h.currentPlayer == p:
        I = getInformationSet(h,p)
        actions=getActions(h)
        if I not in treeMap:
            initializeInfoset(I,h,len(actions))
        strategyI = calculateStrategy(I)

        value = 0
        _value = []
        for i,action in enumerate(actions):
            if treeMap[I][0][i] > C:   
                _h=Node(h=h)                        #update value with C > -300,000,000
                doAction(_h,action)
                _value.append(traverseMCCFR_P(_h,p))
                value += strategyI[i] * _value[i]
            else:
                _value.append(None)
        
        #for i,action in enumerate(actions):
        updateRegrets(I,value,_value)
        return value
    else:
        Ph = h.currentPlayer
        I = getInformationSet(h,Ph)
        actions = getActions(h)
        if I not in treeMap:
            initializeInfoset(I,h,len(actions))
        strategyI = calculateStrategy(I)
        
        index = chooseActionFromStrategy(strategyI)
        doAction(h, actions[index])
        return traverseMCCFR_P(h,p)

def traverseMCCFR(h,p):
    if isTerminal(h):
        #h2 = calculateWinner(h)
        utility = getUtility(h,p)
        return utility
    elif h.pFolded[p]:
        return regretifFolded(h,p)
    elif ischanceNode(h):
        nextRound(h)
        return traverseMCCFR(h,p)
    elif h.currentPlayer == p:
        I = getInformationSet(h,p)
        actions=getActions(h)
        if I not in treeMap:
            initializeInfoset(I,h,len(actions))
        strategyI = calculateStrategy(I)

        value = 0
        _value = []
        for i,action in enumerate(actions):
            _h=Node(h=h)
            doAction(_h,action)
            _value.append(traverseMCCFR(_h,p))
            value += strategyI[i] * _value[i]
        
        #for i,action in enumerate(actions):
        updateRegrets(I,value,_value)
        return value
    else:
        Ph = h.currentPlayer
        I = getInformationSet(h,Ph)
        actions=getActions(h)
        if I not in treeMap:
            initializeInfoset(I,h,len(actions))
        strategyI = calculateStrategy(I)

        index = chooseActionFromStrategy(strategyI)
        if to_print==True:
            print("Available and chosen action: ",actions,index)
        doAction(h, actions[index])
        return traverseMCCFR(h,p)

def MCCFR_P(minutes=1):
    #for p in PLAYERS:
    #map(lambda key : processInfoset(key), treeMap.keys())           ## not required because we are only storing infosets which we are encontering 

    start = datetime.datetime.now().timestamp()
    iterations = 0
    t = 0
    discounted = 0
    while (t / 60 < minutes):
        #print('Iteration: ',iterations)
        t = datetime.datetime.now().timestamp() - start
        iterations += 1

        if (iterations % 1000 == 0):                   
            print("iterations", iterations, "time", round(t))
        
        deck = getshuffledDeck()
        rootN = Node(deck=deck)

        for p in PLAYERS:
            rootNode=Node(h=rootN)
            if iterations % STRATEGY_INTERVAL == 0:
                print("Updating Strategy")
                rootNode_copy=Node(h=rootN)
                updateStrategy(rootNode_copy, p)

            if t / 60 > PRUNE_THRESHOLD:
                q = random.random()
                if (q < 0.05):
                    traverseMCCFR(rootNode,p)
                else:
                    traverseMCCFR_P(rootNode,p)
            else:
                traverseMCCFR(rootNode,p)

        m = int(t / 60)
        if ( m < LCFR_THRESHOLD) and (m % DISCOUNT_INTERVAL == 0) and m!=discounted:
            print('Discounting Strategy')
            discounted = m
            d = (m / DISCOUNT_INTERVAL) / (m / DISCOUNT_INTERVAL + 1)
            #for p in PLAYERS:
            for key in treeMap.keys():
                discountRegrets(key,d)
            #list(map(lambda key : discountRegrets(key,d), treeMap.keys()))
    
    print("Done")
    print(len(treeMap.keys()))
    return 0

#MCCFR_P(minutes=10)
#print(1==BETTING_ROUND_FLOP)
"""
deck= getshuffledDeck()
a=Node(deck=deck)
print(a.get_values())
"""


### checking approx number of action sequences
start = datetime.datetime.now().timestamp()
def getnum_actionSequence(h):
    numActionSequence=0
    t = datetime.datetime.now().timestamp() - start
    if(t/60>240):
        print("Time Finish")
        return 1
    if isTerminal(h):
        lengthactionHistory=len(h.actionHistory)
        if(lengthactionHistory>35):
            print("Length Action History: ",lengthactionHistory)
        return 1
    elif ischanceNode(h):
        nextRound(h)
        numActionSequence+=getnum_actionSequence(h)
    else:
        actions=getActions(h)
        for action in actions:
            _h=Node(h=h)
            doAction(_h, action)
            numActionSequence+=getnum_actionSequence(_h)
    return numActionSequence

"""
deck = getshuffledDeck()
rootN = Node(deck=deck)
numActionSequence=getnum_actionSequence(rootN)
print(numActionSequence)
"""