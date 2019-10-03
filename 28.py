def main():
    n = 1001 // 2
    print(1 + 4 * sum(4 * i**2 + i + 1 for i in range(1, n+1)))


if __name__ == "__main__":
    main()
