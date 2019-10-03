import math


def lattice_paths(n):
    return math.factorial(2 * n) // (math.factorial(n))**2


def main():
    print(lattice_paths(2))
    print(lattice_paths(20))


if __name__ == "__main__":
    main()
