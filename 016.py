def digit_sum(n):
    return sum(map(int, str(n)))


def main():
    print(digit_sum(2**1000))


if __name__ == "__main__":
    main()
