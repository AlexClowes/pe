from math import floor, sqrt


def cont_frac_cycle_length(n):
    k = 0
    mk = 0
    dk = 1
    a0 = ak = floor(sqrt(n))

    # Check for square numbers
    if a0 * a0 == n:
        return 0

    previous_triples = {}
    while (mk, dk, ak) not in previous_triples:
        previous_triples[(mk, dk, ak)] = k
        k += 1
        mk = ak * dk - mk
        dk = (n - mk * mk) // dk
        ak = floor((a0 + mk) // dk)
    return k - previous_triples[(mk, dk, ak)]


def main():
    print(sum(cont_frac_cycle_length(n) % 2 == 1 for n in range(2, 10001)))

if __name__ == "__main__":
    main()
