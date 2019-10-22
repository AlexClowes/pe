from fractions import Fraction


def root_two_cont_fracs():
    frac_part = Fraction(0)
    while True:
        frac_part = 1 / (2 + frac_part)
        yield 1 + frac_part


def main():
    counter = 0
    for i, frac in enumerate(root_two_cont_fracs()):
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            counter += 1
        if i == 10**3:
            break
    print(counter)


if __name__ == "__main__":
    main()
