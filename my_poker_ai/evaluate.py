import itertools
def check_four_of_a_kind(numbers):
    for i in numbers:
        if numbers.count(i) == 4:
            four = i
        elif numbers.count(i) == 1:
            card = i
    score = 105 + four + card/100
    return score

def check_full_house(numbers):
    for i in numbers:
        if numbers.count(i) == 3:
            full = i
        elif numbers.count(i) == 2:
            p = i
    score = 90 + full + p/100  
    return score

def check_three_of_a_kind(numbers):
    cards = []
    for i in numbers:
        if numbers.count(i) == 3:
            three = i
        else: 
            cards.append(i)
    return 45 + three + cards[0]/100 + cards[-1]/1000

def check_two_pair(numbers):
    pairs = []
    cards = []
    for i in numbers:
        if numbers.count(i) == 2:
            pairs.append(i)
        elif numbers.count(i) == 1:
            cards.append(i)
    score = 30 + pairs[0] + pairs[-1]/100 + cards[0]/1000
    return score

def check_pair(numbers):    
    pair = []
    cards  = []
    for i in numbers:
        if numbers.count(i) == 2:
            pair.append(i)
        elif numbers.count(i) == 1:    
            cards.append(i)
    score = 15 + pair[0] + cards[0]/100 + cards[1]/1000 + cards[2]/10000
    return score

def get_num_card(card):
    num=card[0]
    if num=='T':
        return 10
    elif num=='J':
        return 11
    elif num=='Q':
        return 12
    elif num=='K':
        return 13
    else:
        return int(num)

def score_hand(hand):
    letters = [hand[i][1] for i in range(5)] # We get the suit for each card in the hand
    numbers = [get_num_card(hand[i]) for i in range(5)]  # We get the number for each card in the hand
    numbers = sorted(numbers,reverse=True)
    rnum = [numbers.count(i) for i in numbers]  # We count repetitions for each number
    rlet = [letters.count(i) for i in letters]  # We count repetitions for each letter
    dif = numbers[0] - numbers[-1] # The difference between the greater and smaller number in the hand
    handtype = ''
    score = 0
    if 5 in rlet:
        if numbers ==[14,13,12,11,10]:
            handtype = 'royal_flush'
            score = 135
          # print('this hand is a %s:, with score: %s' % (handtype,score))  I comment the prints so the script runs faster 
        elif dif == 4:
            handtype = 'straight_flush'
            score = 120 + numbers[0]
          # print('this hand is a %s:, with score: %s' % (handtype,score)) 
        elif numbers == [14,5,4,3,2]:
            handtype = 'straight_flush'
            return 120
        else:
            handtype = 'flush'
            score = 75 + numbers[0] + numbers[1]/100 + numbers[2]/1000 + numbers[3]/10000 + numbers[4]/100000
          # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    elif 4 in rnum:
        handtype = 'four of a kind'
        score = check_four_of_a_kind(numbers)
      # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    elif sorted(rnum) == [2,2,3,3,3]:
       handtype = 'full house'
       score = check_full_house(numbers)
     # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    elif dif == 4:
        handtype = 'straight'
        score = 60 + numbers[0]
      # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    elif numbers == [14,5,4,3,2]:
        handtype = 'straight'
        return 60
    elif 3 in rnum:
        handtype = 'three of a kind' 
        score = check_three_of_a_kind(numbers)
      # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    elif rnum.count(2) == 4:
        handtype = 'two pair'
        score = check_two_pair(numbers)
      # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    elif rnum.count(2) == 2:
        handtype = 'pair'
        score = check_pair(numbers)
      # print('this hand is a %s:, with score: %s' % (handtype,score)) 
    
    else:
        handtype= 'high card'
        score = numbers[0] + numbers[1]/100 + numbers[2]/1000 + numbers[3]/10000 + numbers[4]/100000
      # print('this hand is a %s:, with score: %s' % (handtype,score))     
    return handtype,score

def evaluate_poker_table(pCards,board):
    scores=[]
    for i,e in enumerate(pCards):
        hands=[list(e) for e in itertools.combinations(e+board,5)]
        scores.append(evaluate_player_hand(hands))
    return scores

def evaluate_player_hand(hands):
    #scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]
    scores = [(i, score(hand)) for i, hand in enumerate(hands)]
    winners = sorted(scores , key=lambda x:x[1])
    return winners[-1][1]

def score(hand):
    ranks = '23456789TJQKA'
    rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    #print(rcounts, ranks)
    if len(score) == 5:
        if ranks[0:2] == (12, 3): #adjust if 5 high straight
            ranks = (3, 2, 1, 0, -1)
        straight = ranks[0] - ranks[4] == 4
        flush = len({suit for _, suit in hand}) == 1
        '''no pair, straight, flush, or straight flush'''
        score = ([(1,), (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
    elif len({suit for _, suit in hand}) == 1:
        score = (3,1,1,2)
        ranks_flush = sorted([[rank,cnt] for rank, cnt in rcounts],reverse=True)
        ranks=[]
        for e in ranks_flush:
            ranks.extend(e) 
        ranks=tuple(ranks)
    return score, ranks

#print(evaluate_player_hand(['8C TC 4C 9C 4C', '8C TS KC 9H 4S', '8C AD 8D AC 9C', '7C 5H 8D TD KS']))

#print(evaluate_poker_table([['8C','TC'],['4C','QC']],['8C','TC','4C','9C','4C']))
#print(evaluate_player_hand([['8C','TC','4C','9C','4C']]))
