def count_coin_sums(target, coins):
    if target == 0:
        return 1
    if not coins:
        return 0
    return sum(
        count_coin_sums(target - i * coins[-1], coins[:-1])
        for i in range(target // coins[-1] + 1)
    )


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print(count_coin_sums(200, coins))


if __name__ == "__main__":
    main()
