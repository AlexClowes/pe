from math import floor, sqrt


def gen_sqrt_cont_frac_terms(n):
    mk = 0
    dk = 1
    a0 = ak = floor(sqrt(n))
    while True:
        yield ak
        mk = ak * dk - mk
        dk = (n - mk * mk) // dk
        ak = floor((a0 + mk) // dk)


def gen_convergents(n):
    cont_frac_terms = gen_sqrt_cont_frac_terms(n)
    p1, q1 = 1, 0
    p2, q2 = next(cont_frac_terms), 1
    yield p2, q2

    while True:
        a = next(cont_frac_terms)
        p3 = a * p2 + p1
        q3 = a * q2 + q1
        yield p3, q3
        p1, q1 = p2, q2
        p2, q2 = p3, q3


def main():
    max_x = 0
    for D in range(2, 1001):
        if floor(sqrt(D))**2 == D:
            continue
        for x, y in gen_convergents(D):
            if x * x - D * y * y == 1:
                if x > max_x:
                    max_x = x
                    best_D = D
                break
    print(best_D)


if __name__ == "__main__":
    main()
