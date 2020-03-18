from functools import lru_cache


@lru_cache(maxsize=None)
def count_prize_strings(days_left, absences=0, lates=0):
    if absences == 3 or lates == 2:
        return 0
    if days_left == 0:
        return 1
    return (
        count_prize_strings(days_left - 1, 0, lates)
        + count_prize_strings(days_left - 1, absences + 1, lates)
        + count_prize_strings(days_left - 1, 0, lates + 1)
    )


def main():
    print(count_prize_strings(30))


if __name__ == "__main__":
    main()
