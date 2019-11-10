from itertools import combinations
from math import factorial


def prod(it):
    p = 1
    for el in it:
        p *= el
    return p


def ways_to_lose(n_turns):
    total = 0
    for n_lose_turns in range((n_turns + 1) // 2, n_turns + 1):
        for lose_turns in combinations(range(1, n_turns + 1), n_lose_turns):
            total += prod(lose_turns)
    return total


def main():
    n_turns = 15
    games = factorial(n_turns + 1)
    print(games // (games - ways_to_lose(n_turns)))


if __name__ == "__main__":
    main()
