from math import ceil, log2


def p(L, n):
    lower_bound, upper_bound = log2(L), log2(L + 1)
    log210 = log2(10)
    ret = 0
    mid = 0
    count = 0
    while count < n:
        if mid < lower_bound:
            inc = ceil(lower_bound - mid)
            ret += inc
            mid += inc
        if mid < upper_bound:
            count += 1
        mid -= log210
    return ret


def main():
    print(p(123, 678910))


if __name__ == "__main__":
    main()
