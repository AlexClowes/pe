def tetr(a, b, mod):
    ret = a
    for _ in range(1, b):
        ret = pow(a, ret, mod)
    return ret


def main():
    print(tetr(1777, 1855, 10 ** 8))


if __name__ == "__main__":
    main()
