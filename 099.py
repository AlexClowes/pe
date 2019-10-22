from math import log


def main():
    with open("data/p099_base_exp.txt") as f:
        base_exp_pairs = [line.strip().split(",") for line in f]
    base_exp_pairs = [(int(base), int(exp)) for base, exp in base_exp_pairs]
    biggest_val = 0
    for i, (base, exp) in enumerate(base_exp_pairs, 1):
        if exp * log(base) > biggest_val:
            biggest_val = exp * log(base)
            biggest_line = i
    print(biggest_line)


if __name__ == "__main__":
    main()
