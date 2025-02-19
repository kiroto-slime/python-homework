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
