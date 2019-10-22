def digit_fifth_power_sum(n):
    return sum(int(digit)**5 for digit in str(n))


def main():
    total = 0
    for n in range(2, 10**6):
        if n == digit_fifth_power_sum(n):
            total += n
    print(total)


if __name__ == "__main__":
    main()
