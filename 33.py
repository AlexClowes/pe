from fractions import Fraction


def cancel(num, den):
    num = list(str(num))
    den = list(str(den))
    done = False
    for i in range(2):
        for j in range(2):
            if not done and num[i] == den[j] and num[i] != 0:
                del num[i]
                del den[j]
                done = True
    num = int(''.join(num))
    den = int(''.join(den))
    return num, den


def main():
    prod = Fraction(1, 1)
    for num in range(10, 99):
        for den in range(num + 1, 100):
            c_num, c_den = cancel(num, den)
            if num != c_num and num / den == c_num / c_den:
                prod *= Fraction(num, den)
                print(num, den, c_num, c_den)
    print(prod)


if __name__ == "__main__":
    main()
