import itertools
def convert_card(card_number):
    suits = ["黑桃", "紅桃", "方塊", "梅花"]
    suit = suits[(card_number - 1) // 13]
    rank = (card_number - 1) % 13 + 1
    return (suit, rank)
def evaluate_hand(hand):
    suits = [card[0] for card in hand]#花色
    ranks = sorted([card[1] for card in hand])#點數
    #計算點數出現次數
    rank_counts = {rank:ranks.count(rank) for rank in set(ranks)}
    rank_frequencies = sorted(rank_counts.values(), reverse=True)
    #判斷各種牌型
    is_flush = len(set(suits)) == 1#花色相同
    is_straight = ranks == list(range(ranks[0], ranks[0] + 5)) or ranks == [1, 10, 11, 12, 13]#順子
    if is_flush and is_straight:
        return 7#同花順
    elif 4 in rank_frequencies:
        return 6#四條
    elif rank_frequencies == [3, 2]:
        return 5#葫蘆
    elif is_straight:
        return 4#順子
    elif 3 in rank_frequencies:
        return 3#三條
    elif rank_frequencies == [2, 2, 1]:
        return 2#兩對
    elif 2 in rank_frequencies:
        return 1#一對
    else:
        return 0#雜牌
n = int(input())
results = []
for i in range(n):
    cards = list(map(int, input().split()))
    converted_cards = [convert_card(card) for card in cards]
    max_score = 0
    for hand in itertools.combinations(converted_cards, 5):
        score = evaluate_hand(hand)
        max_score = max(max_score, score)
    results.append(str(max_score))
print("\n".join(results))
