from math import floor, sqrt


def is_square(n):
    return floor(sqrt(n))**2 == n


def main():
    target = 10 ** 6
    total = 0
    x = 0
    while total < target:
        x += 1
        for yz_sum in range(2, 2 * x + 1):
            if is_square(x * x + yz_sum * yz_sum):
                total += (x + 1) // 2 - abs(x + 1 - yz_sum) // 2
    print(x)



if __name__ == "__main__":
    main()

