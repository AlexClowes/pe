from utils import is_prime


def main():
    N = 10 ** 6
    r = 1
    count = 0
    while True:
        candidate = 3 * r * r + 3 * r + 1
        if candidate > N:
            break
        count += is_prime(candidate)
        r += 1
    print(count)


if __name__ == "__main__":
    main()
