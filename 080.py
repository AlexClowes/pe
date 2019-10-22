from math import floor, sqrt


def digit_sum(n):
    return sum(map(int, str(n)))


def square_root_digit_sum(n, places=100):
   p = floor(sqrt(n))
   q = 1
   while q < 10 ** (places - 1):
       p, q = p * p + n * q * q, 2 * p * q
   return digit_sum(p * 10 ** (places - 1) // q)


def main():
    total = 0
    for n in range(2, 101):
        if floor(sqrt(n))**2 != n:
            total += square_root_digit_sum(n)
    print(total)


if __name__ == "__main__":
    main()
