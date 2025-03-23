from itertools import combinations
from collections import Counter
poker_hands= {
    (4, 1): 6, #四條
    (3, 2): 5, #葫蘆
    (3, 1, 1): 3, #三條
    (2, 2, 1): 2, #兩對
    (2, 1, 1, 1): 1, #一對
    (1, 1, 1, 1, 1): 0 #雜牌
}
def hand_score(combo):
    suits= {(c-1) // 13 for c in combo} #花色
    ranks= sorted((c-1) % 13+1 for c in combo) #點數
    times= tuple(sorted(Counter(ranks).values(), reverse=True))
    flush= len(suits)== 1 #同花
    straight= (
        len(set(ranks))== 5 
        and (ranks[-1]-ranks[0]== 4
                or ranks== [1, 2, 3, 4, 5]
                or ranks== [1, 10, 11, 12, 13])
    )#順子
    if flush and straight: #同花順
        return 7
    base_score= poker_hands[times]
    if straight:
        return max(base_score, 4)
    return base_score
t= int(input())
for i in range(t):
    cards= list(map(int, input().split()))
    print(max(hand_score(combo) for combo in combinations(cards, 5)))
