def is_pandigital(n):
    return sorted(map(int, n)) == list(range(1, len(n) + 1))


def concat_prods(n):
    ret = str(n)
    i = 2
    while len(ret) < 9:
        ret += str(i * n)
        i += 1
    return ret


def main():
    biggest_pand = 0
    for n in range(1, 10**4):
        candidate = concat_prods(n)
        if len(candidate) == 9 and is_pandigital(candidate) and int(candidate) > biggest_pand:
            biggest_pand = int(candidate)
    print(biggest_pand)



if __name__ == "__main__":
    main()
