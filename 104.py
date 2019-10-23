from math import sqrt


def is_pandigital(string):
    return "".join(sorted(string)) == "123456789"


def main():
    fn_1, fn_2 = 1, 1
    n = 2
    while True:
        n += 1
        fn_1, fn_2 = fn_2, (fn_1 + fn_2) % 10 ** 9
        if is_pandigital(str(fn_2)):
            phi = (1 + sqrt(5)) / 2
            fib_approx = 1 / sqrt(5)
            for _ in range(n):
                if fib_approx > 10 ** 20:
                    fib_approx /= 10 ** 10
                fib_approx *= phi
            if is_pandigital(str(fib_approx)[:9]):
                print(n)
                return


if __name__ == "__main__":
    main()

