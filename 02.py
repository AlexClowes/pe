def main():
    old1 = 1
    old2 = 1
    new = -1
    total = 0
    while new <= 4 * 10**6:
        new = old1 + old2
        old1, old2 = old2, new
        if new % 2 == 0:
            total += new
    print(total)


if __name__ == "__main__":
    main()
