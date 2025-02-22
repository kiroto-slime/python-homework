def do_card(num):
    suits= ["黑桃", "紅桃", "方塊", "梅花"]
    suit= suits[(num-1)//13]
    rank= (num-1)%13+1
    return (suit, rank)
def calc_cardss(cardss):
    suits= [card[0] for card in cardss]
    ranks= sorted([card[1] for card in cardss])
    rank_counts= {rank: ranks.count(rank) for rank in set(ranks)}
    rank_times= sorted(rank_counts.values(), reverse=True)
    straight=ranks== list(range(ranks[0], ranks[0]+5)) or ranks== [1, 10, 11, 12, 13]
    flush= len(set(suits))== 1
    if flush and straight:
        return "同花順"
    elif 4 in rank_times:
        return "四條"
    elif rank_times== [3, 2]:
        return "葫蘆"
    elif straight:
        return "順子"
    elif 3 in rank_times:
        return "三條"
    elif rank_times== [2, 2, 1]:
        return "兩對"
    elif 2 in rank_times:
        return "一對"
    else:
        return "雜牌"
times= int(input())
results=[]
for i in range(times):
    cards= list(map(int, input().split()))
    x= [do_card(card) for card in cards]
    s= calc_cardss(x)
    results.append(s)
print("\n".join(results))
