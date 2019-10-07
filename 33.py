from fractions import Fraction


def cancel(num, den):
    num_digits = divmod(num, 10)
    den_digits = divmod(den, 10)
    for i in range(2):
        for j in range(2):
            if num_digits[i] == den_digits[j]:
                return num_digits[(i + 1) % 2], den_digits[(j + 1) % 2]
    return num, den


def main():
    product = Fraction(1)
    for p in range(10, 100):
        if p % 10 == 0:
            continue
        for q in range(p + 1, 100):
            if q % 10 == 0:
                continue
            p_c, q_c = cancel(p, q)
            if p != p_c and p * q_c == p_c * q:
                product *= Fraction(p, q)
    print(product)



if __name__ == "__main__":
    main()
