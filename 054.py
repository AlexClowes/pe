from collections import Counter
from enum import IntEnum, unique


def gen_games():
    with open("data/p054_poker.txt") as f:
        for line in f:
            cards = line.strip().split(" ")
            yield cards[:5], cards[5:]


@unique
class Quality(IntEnum):
    high_card = 0
    one_pair = 1
    two_pairs = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8


def canonical_form(hand):
    flush = (len(set(card[1] for card in hand)) == 1)
    ranks = sorted("23456789TJQKA".find(card[0]) for card in hand)
    straight = (ranks == list(range(ranks[0], ranks[0] + 5)))
    rank_count = Counter(ranks)
    distinct_counts = sorted(rank_count.values())
    distinct_ranks = sorted(rank_count, reverse=True, key=lambda r: (rank_count[r], r))
    if flush and straight:
        q = Quality.straight_flush
    elif distinct_counts == [1, 4]:
        q = Quality.four_of_a_kind
    elif distinct_counts == [2, 3]:
        q = Quality.four_of_a_kind
    elif flush:
        q = Quality.flush
    elif straight:
        q = Quality.straight
    elif distinct_counts == [1, 1, 3]:
        q = Quality.three_of_a_kind
    elif distinct_counts == [1, 2, 2]:
        q = Quality.two_pairs
    elif distinct_counts == [1, 1, 1, 2]:
        q = Quality.one_pair
    else:
        q = Quality.high_card
    return q, distinct_ranks


def main():
    games = gen_games()
    p1_wins = (canonical_form(hand1) > canonical_form(hand2) for hand1, hand2 in games)
    print(sum(p1_wins))


if __name__ == "__main__":
    main()
