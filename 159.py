from itertools import count


def digital_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total if total < 10 else digital_sum(total)


def sum_mdrs(n_max):
    mdrs = [digital_sum(n) for n in range(n_max)]
    for n in count(2):
        if n * n >= n_max:
            break
        for i in count():
            if n * n + i * n >= n_max:
                break
            mdrs[n * n + i * n] = max(mdrs[n * n + i * n], mdrs[n] + mdrs[n + i])
    return sum(mdrs[2:])


def main():
    print(sum_mdrs(10 ** 6))


if __name__ == "__main__":
    main()
