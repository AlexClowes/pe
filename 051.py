from itertools import product

from utils import get_primes_up_to_n, is_prime


def get_replacement_family(digits):
    for r in [chr(i) for i in range(ord("0"), ord("9") + 1)]:
        if digits[0] == "*" and r == "0":
            continue
        yield int("".join([d if d != "*" else r for d in digits]))


def main():
    primes = list(get_primes_up_to_n(10**6))
    done = False
    for p in primes:
        digits = str(p)
        unique_digits = set(digits)
        for u_digit in unique_digits:
            p_with_asterisks = [
                p_digit if p_digit != u_digit else "*"
                for p_digit in digits
            ]
            rep_family = list(filter(is_prime, get_replacement_family(p_with_asterisks)))
            if len(rep_family) == 8:
                print(min(rep_family))
                done = True
                break
        if done:
            break



if __name__ == "__main__":
    main()
