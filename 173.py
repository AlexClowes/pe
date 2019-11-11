def main():
    N = 10 ** 6
    total = 0
    for m in range(3, N // 4 + 2):
        for n in range(m - 2, 0, -2):
            if m ** 2 - n ** 2 > N:
                break
            total += 1
    print(total)


if __name__ == "__main__":
    main()
