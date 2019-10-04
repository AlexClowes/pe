def fact(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod


factorials = [fact(n) for n in range(10)]
def digit_factorial_sum(n):
    digits = map(int, str(n))
    return sum(map(lambda n: factorials[n], digits))


def main():
    total = 0
    for n in range(3, 10**7):
        if n == digit_factorial_sum(n):
            total += n
    print(total)


if __name__ == "__main__":
    main()
