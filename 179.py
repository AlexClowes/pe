def main():
    N = 10 ** 7
    div_count = [1] * N
    for i in range(2, N):
        if div_count[i] == 1:
            prime_pow = prime = i
            exponent = 1
            while prime_pow < N:
                for j in range(prime_pow, N, prime_pow):
                    div_count[j] *= exponent + 1
                    if exponent != 1:
                        div_count[j] //= exponent
                prime_pow *= prime
                exponent += 1

    count = 0
    for i in range(2, N - 1):
        if div_count[i] == div_count[i + 1]:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
