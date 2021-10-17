#Pre-final-round
## Prerequisites: Strategy for grouping similar hands together.
## Earth mover feature for every possible cards for each round. 

## Prerequisites: Earth mover feature for every possible cards for each round. 
## Create buckets using k-means clustering for each round using earth mover distance.

## Prerequisites: Stored cultered data.
## Get bucket number for each card set from stored culstered data. 

#Final-round
## Prerequisites: Strategy for grouping similar hands together, 8 clusters  
## OHCS for every possible cards for each round. 

## Prerequisites: OHCS for every possible cards for each round. 
## Create buckets using k-means clustering for each round using earth mover distance. 

## Prerequisites: Stored cultered data. 
## Get bucket number for each card set from stored culstered data. 


# To do strategy for grouping similar hand together, basically strategy for lossless abstraction
import sys
sys.path.append('../')
import main1 as traverse_actions
from evaluate import evaluate_poker_table
import copy
import matplotlib.pyplot as plt

# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f
cardspersuit=['8','9','T','J','Q','K','A']
# cardspersuit=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits=['c','d','h','s']
#suits=['d','h','s']

num_suits=len(suits)
num_cards_suit=len(cardspersuit)
print(num_suits,num_cards_suit)

def calculate_value(deck,num_cards,hand,value):
    #print(num_cards)
    deck=copy.deepcopy(deck)
    if num_cards==9:
        value[1]+=1
        scores=evaluate_poker_table([[hand[0],hand[1]], [hand[7],hand[8]]], hand[2:7])
        #print(scores)
        if scores[0]>scores[1]:
            value[0]+=1
        elif scores[0]==scores[1]:
            value[0]+=.5
        return 

    for i in range(num_suits):
        for j in range(num_cards_suit):
            if deck[i][j]==1:
                deck[i][j]=0
                hand.append(cardspersuit[j]+suits[i])
                calculate_value(deck,num_cards+1,hand,value)

                hand.pop()
    return 

def pnc_board(deck,num_cards,hand,deck_copy,feature):  
    #print(num_cards)
    deck=copy.deepcopy(deck)
    if num_cards==7:
        # feature[0]+=1
        value=[0,0]
        calculate_value(deck_copy,num_cards,hand,value)
        idx=int(value[0]/value[1]*20)
        #print(value[0],value[1],idx)
        if idx==20:
            idx=19
        assert (idx>=0 and idx<20), "feature index out of scope"
        if sum(feature)%100==0:
            print(sum(feature))
        feature[idx]+=1
        return 

    for i in range(num_suits):
        for j in range(num_cards_suit):
            if deck[i][j]==1:
                deck[i][j]=0
                deck_copy[i][j]=0
                hand.append(cardspersuit[j]+suits[i])
                pnc_board(deck,num_cards+1,hand,deck_copy,feature)

                deck_copy[i][j]=1
                hand.pop()
    return 

def getDeckMatrix():
    cardspersuit=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits=['c','d','h','s']
    deck=[]
    mapping=[]
    for suit in suits:
        mapping.append([card+suit for card in cardspersuit])
        deck.append([1 for card in cardspersuit])
    return mapping,deck


def calculate_features():
    deck = [[1]*num_cards_suit for i in range(num_suits)]
    hand = []
    #Round 1
    round = 0
    result = [[None]*num_cards_suit for i in range(num_cards_suit)]

    for i in range(num_cards_suit):
        for j in range(num_cards_suit):
            feature = [0 for i in range(20)]
            deck[0][i]=0
            hand.append(cardspersuit[i]+suits[0])
            if j>=i:
                deck[1][j]=0
                hand.append(cardspersuit[j]+suits[1])
                pnc_board(deck,2,hand,copy.deepcopy(deck),feature)

                deck[1][j]=1
            else:
                deck[0][j]=0
                hand.append(cardspersuit[j]+suits[0])
                pnc_board(deck,2,hand,copy.deepcopy(deck),feature)

                deck[0][j]=1

            hand.pop()
            hand.pop()
            deck[0][i]=0
            
            result[i][j]=[feature[i]/sum(feature) for i in range(len(feature))]
            print(result)

        
def calculate_features_test():
    deck = [[1]*num_cards_suit for i in range(num_suits)]
    hand = []
    #Round 1
    round = 0
    result = [[None]*num_cards_suit for i in range(num_cards_suit)]

    for i in range(5,6):
        for j in range(5,6):
            feature = [0 for i in range(20)]
            deck[0][i]=0
            hand.append(cardspersuit[i]+suits[0])
            if j>=i:
                deck[1][j]=0
                hand.append(cardspersuit[j]+suits[1])
                pnc_board(deck,2,hand,copy.deepcopy(deck),feature)

                deck[1][j]=1
            else:
                deck[0][j]=0
                hand.append(cardspersuit[j]+suits[0])
                pnc_board(deck,2,hand,copy.deepcopy(deck),feature)

                deck[0][j]=1

            hand.pop()
            hand.pop()
            deck[0][i]=0
            
            print(sum(feature))
            result[i][j]=[feature[i]/sum(feature) for i in range(len(feature))]
            print(result[i][j])
            plt.bar(range(20), result[i][j])

calculate_features_test()

            


