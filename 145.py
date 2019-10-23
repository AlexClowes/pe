def main():
    total = 0
    for n in range(1, 10):
        if n % 2 == 0:
            total += 20 * 30 ** (n // 2 - 1)
        elif n % 4 == 3:
            total += 100 * 500 ** (n // 4)
    print(total)


if __name__ == "__main__":
    main()
