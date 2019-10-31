from collections import Counter
from fractions import Fraction
from itertools import product


def dice_probs(n_dice, dice_val):
    rolls = map(sum, product(range(1, dice_val + 1), repeat=n_dice))
    counts = Counter(rolls)
    return {k :Fraction(v, dice_val ** n_dice) for k, v in counts.items()}


def main():
    pete_probs = dice_probs(9, 4)
    colin_probs = dice_probs(6, 6)

    pete_win_prob = Fraction(0)
    for pete_score, pete_prob in pete_probs.items():
        for colin_score, colin_prob in colin_probs.items():
            if pete_score > colin_score:
                pete_win_prob += pete_prob * colin_prob
    print(round(float(pete_win_prob), 7))


if __name__ == "__main__":
    main()
