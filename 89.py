NUMERAL_VALS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def roman_to_int(numeral):
    pos = 0
    n = 0
    while pos < len(numeral):
        if numeral[pos:pos + 2] in NUMERAL_VALS:
            n += NUMERAL_VALS[numeral[pos:pos+2]]
            pos += 2
        else:
            n += NUMERAL_VALS[numeral[pos]]
            pos += 1
    return n

def int_to_roman(n):
    numerals = []
    while n > 0:
        for numeral, val in NUMERAL_VALS.items():
            if n >= val:
                numerals.append(numeral)
                n -= val
                break
    return "".join(numerals)


def main():
    with open("data/p089_roman.txt") as f:
        old_numerals = f.read().split()

    new_numerals = [int_to_roman(roman_to_int(numeral)) for numeral in old_numerals]
    print(sum(len(old) - len(new) for old, new in zip(old_numerals, new_numerals)))


if __name__ == "__main__":
    main()
