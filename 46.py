import math

from utils import is_prime


def main():
    candidate = 7
    while True:
        candidate += 2
        if is_prime(candidate):
            continue
        for i in range(1, math.ceil(math.sqrt(candidate / 2))):
            if is_prime(candidate - 2 * i ** 2):
                break
        else:
            print(candidate)
            break


if __name__ == "__main__":
    main()
