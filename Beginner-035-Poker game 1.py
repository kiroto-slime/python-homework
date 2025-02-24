import itertools
def do_card(num):
    suits= ["黑桃", "紅桃", "方塊", "梅花"]
    suit= suits[(num-1)//13]
    rank= (num-1)%13+1
    return (suit, rank)
def calc_cardss(cardss):
    suits= [card[0] for card in cardss]#花色
    ranks= sorted([card[1] for card in cardss])#點數
    rank_counts= {rank:ranks.count(rank) for rank in set(ranks)}#次數
    rank_times= sorted(rank_counts.values(), reverse= True)#頻率
    flush= len(set(suits))==1#同花
    straight= ranks==list(range(ranks[0], ranks[0]+5)) or ranks==[1, 10, 11, 12, 13]#順子
    if flush and straight:
        return 7#同花順
    elif 4 in rank_times:
        return 6#四條
    elif rank_times==[3, 2]:
        return 5#葫蘆
    elif straight:
        return 4#順子
    elif 3 in rank_times:
        return 3#三條
    elif rank_times==[2, 2, 1]:
        return 2#兩對
    elif 2 in rank_times:
        return 1#一對
    else:
        return 0#雜牌
n= int(input())
for i in range(n):
    cards= list(map(int, input().split()))
    do_cards= [do_card(card) for card in cards]
    max_s= 0
    for e in itertools.combinations(do_cards, 5):
        s= calc_cardss(e)
        max_s= max(max_s, s)
    print(max_s)
#another
from itertools import combinations
from collections import Counter
freq2score={(4,1):6,(3,2):5,(3,1,1):3,(2,2,1):2,(2,1,1,1):1,(1,1,1,1,1):0}
score_map={
    (f,fl,st):(fl and st)*7+(not(fl and st))*max(freq2score[f],4*fl,4*st)
    for f in freq2score
    for fl in [False,True]
    for st in [False,True]
}
t=int(input())
for _ in range(t):
    cards=list(map(int,input().split()))
    best=0
    for combo in combinations(cards,5):
        s=[(c-1)//13 for c in combo]
        r=sorted((c-1)%13+1 for c in combo)
        fl=len(set(s))==1
        st=(len(set(r))==5 and r[-1]-r[0]==4)or r==[1,10,11,12,13]
        freq=tuple(sorted(Counter(r).values(),reverse=True))
        score=score_map[(freq,fl,st)]
        if score>best:best=score
    print(best)
