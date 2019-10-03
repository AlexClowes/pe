def sum_multiples_up_to_bound(k, u_bound):
    n_multiples = (u_bound - 1) // k
    return k * n_multiples * (n_multiples + 1) // 2


def main():
    result = (
        sum_multiples_up_to_bound(3, 1000)
        + sum_multiples_up_to_bound(5, 1000)
        - sum_multiples_up_to_bound(15, 1000)
    )
    print(result)


if __name__ == "__main__":
    main()
