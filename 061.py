from collections import defaultdict


def recurse(cycle, remaining_keys, nums):
    if not remaining_keys:
        if cycle[0] // 100 == cycle[-1] % 100:
            return cycle
        return False
    for key in remaining_keys:
        for n in nums[key]:
            if not cycle or n // 100 == cycle[-1] % 100:
                new_cycle = recurse(cycle + [n], remaining_keys - {key}, nums)
                if new_cycle:
                    return new_cycle
    return False


def main():
    funcs = {
        "tri": lambda n: n * (n + 1) // 2,
        "sqr": lambda n: n * n,
        "pen": lambda n: n * (3 * n - 1) // 2,
        "hex": lambda n: n * (2 * n - 1),
        "hep": lambda n: n * (5 * n - 3) // 2,
        "oct": lambda n: n * (3 * n - 2),
    }
    nums = defaultdict(list)
    for k, f in funcs.items():
        n = 1
        fn = f(1)
        fn = f(1)
        while fn < 10 ** 4:
            if fn >= 10 ** 3:
                nums[k].append(fn)
            n += 1
            fn = f(n)

    print(sum(recurse([], set(nums.keys()), nums)))


if __name__ == "__main__":
    main()
