from utils import get_partition_count


def main():
    n = 1
    while get_partition_count(n) % 10 ** 6 != 0:
        n += 1
    print(n)


if __name__ == "__main__":
    main()
