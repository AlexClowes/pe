from itertools import combinations


def is_valid(seq):
    unique_sums = set()
    max_sum = max(seq)
    for subset_size in range(2, len(seq)):
        subsets = combinations(seq, subset_size)
        subset_sums = map(sum, subsets)
        for s in subset_sums:
            if s in unique_sums:
                return False
            unique_sums.add(s)
        if min(unique_sums) <= max_sum:
            return False
        max_sum = max(unique_sums)
        unique_sums.clear()
    return True


def main():
    n = 7
    # Guess that all elements of sequence are between 20 and 49
    sequences = combinations(range(20, 50), n)
    min_sum = float("inf")
    for seq in sequences:
        if sum(seq) < min_sum and is_valid(seq):
            min_sum = sum(seq)
            min_seq = seq
    print("".join(str(n) for n in min_seq))


if __name__ == "__main__":
    main()
