from collections import defaultdict
from math import ceil, sqrt


def get_factorisations(n_max):
    factorisations = defaultdict(list)
    for n in range(2, n_max + 1):
        # First get all factorisations using just 2 numbers
        for m in range(2, ceil(sqrt(n + 1))):
            if n % m == 0:
                factorisations[n].append((m, n // m))
        # Now get all the other factorisations, using previous factorisations
        # as a look-up table
        for factorisation in factorisations[n]:
            for i, factor in enumerate(factorisation):
                remaining_factors = factorisation[:i] + factorisation[i+1:]
                for subfactors in factorisations[factor]:
                    new_factorisation = tuple(sorted(subfactors + remaining_factors))
                    if new_factorisation not in factorisations[n]:
                        factorisations[n].append(new_factorisation)
    return factorisations


def main():
    k_max = 12000

    factorisations = get_factorisations(2 * k_max)

    prod_sum_sizes = {
        n: [len(factors) + n - sum(factors) for factors in factor_list]
        for n, factor_list in factorisations.items()
    }

    min_prod_sum = {}
    for n, sizes in prod_sum_sizes.items():
        for size in sizes:
            if size not in min_prod_sum:
                min_prod_sum[size] = n

    print(sum({min_prod_sum[k] for k in range(2, k_max + 1)}))


if __name__ == "__main__":
    main()
