def n_losing_games(exp):
    # Shifted Fibonacci
    a, b = 1, 1
    for _ in range(exp):
        a, b = a + b, a
    return a


def main():
    print(n_losing_games(30))


if __name__ == "__main__":
    main()
