def main():
    N = 1000
    old1, old2 = 1, 1
    new = 2
    idx = 3
    while len(str(new)) < N:
        old1, old2 = old2, new
        new = old1 + old2
        idx += 1
    print(idx)


if __name__ == "__main__":
    main()
