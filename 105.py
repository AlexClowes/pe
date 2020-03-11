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
    with open("data/p105_sets.txt") as f:
        sequences = (tuple(int(n) for n in line.strip().split(",")) for line in f)
        print(sum(sum(seq) for seq in sequences if is_valid(seq)))


if __name__ == "__main__":
    main()
