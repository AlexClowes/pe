def next_lexi_perm(vals):
    i = -1
    for k in range(len(vals) - 1):
        if vals[k] < vals[k + 1]:
            i = k
    if i == -1:
        return vals[::-1]
    j = i + 1
    for k in range(i + 2, len(vals)):
        if vals[k] > vals[i]:
            j = k
    vals[i], vals[j] = vals[j], vals[i]
    vals[i + 1:] = vals[:i:-1]
    return vals



def lexi_perm_gen(n):
    vals = list(range(n))
    while True:
        yield vals
        vals = next_lexi_perm(vals)


def main():
    for i, p in enumerate(lexi_perm_gen(10), 1):
        if i == 10**6:
            print(*p, sep="")
            break


if __name__ == "__main__":
    main()
