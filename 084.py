from collections import Counter
from itertools import islice
from random import randint


def dice_roll():
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    return d1 + d2, d1 == d2


GO = 0
JAIL = 10
G2J = 30
CC = {2, 17, 33}
CH = {7, 22, 36}


def community_chest(pos):
    card = randint(1, 16)
    if card == 1:
        return GO
    if card == 2:
        return JAIL
    return pos


def next_rail(pos):
    if pos < 5 or pos > 35:
        return 5
    if pos < 15:
        return 15
    if pos < 25:
        return 25
    if pos < 35:
        return 35


def next_utility(pos):
    if pos < 12 or pos > 28:
        return 12
    return 28


def chance(pos):
    card = randint(1, 16)
    if card == 1:
        return GO
    if card == 2:
        return JAIL
    if card == 3:
        return 11
    if card == 4:
        return 24
    if card == 5:
        return 39
    if card == 6:
        return 5
    if card in (7, 8):
        return next_rail(pos)
    if card == 9:
        return next_utility(pos)
    if card == 10:
        if pos - 3 in CC:
            return community_chest(pos)
        return pos - 3
    return pos


def next_pos(pos, n_doubles):
    roll, is_double = dice_roll()
    pos = (pos + roll) % 40
    if is_double:
        n_doubles += 1
    else:
        n_doubles = 0

    if n_doubles == 3:
        return JAIL, 0
    if pos == G2J:
        return JAIL, n_doubles
    if pos in CC:
        return community_chest(pos), n_doubles
    if pos in CH:
        return chance(pos), n_doubles
    return pos, n_doubles


def player():
    pos, n_doubles = 0, 0
    while True:
        yield pos
        pos, n_doubles = next_pos(pos, n_doubles)


def main():
    N = 10 ** 6
    count = Counter(islice(player(), N))
    most_common = [pos for pos, _ in count.most_common(3)]
    print(*most_common, sep="")


if __name__ == "__main__":
    main()
