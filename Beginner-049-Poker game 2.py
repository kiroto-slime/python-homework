from collections import Counter
poker_hands= {
    (4, 1): 6,   # 四條
    (3, 2): 5,   # 葫蘆
    (3, 1, 1): 3, # 三條
    (2, 2, 1): 2, # 兩對
    (2, 1, 1, 1): 1, # 一對
    (1, 1, 1, 1, 1): 0 # 雜牌
}
score2name = {
    0: "雜牌",1: "一對",2: "兩對",3: "三條",
    4: "順子",5: "葫蘆",6: "四條",7: "同花順",
}
def hand_name(cards):
    suits= {(c-1)//13 for c in cards}
    ranks= sorted((c-1)%13+1 for c in cards)
    straight= (
        len(set(ranks))== 5 and (
            ranks[-1]-ranks[0]== 4 or
            ranks== [1, 2, 3, 4, 5] or
            ranks== [1, 10, 11, 12, 13]
        )
    )
    flush= len(suits)== 1
    counts= tuple(sorted(Counter(ranks).values(), reverse=True))
    base= poker_hands[counts]
    if flush and straight:
        return score2name[7]
    if straight:
        base= max(base, 4)
    return score2name[base]
t= int(input())
for i in range(t):
    cards= list(map(int, input().split()))
    print(hand_name(cards))
