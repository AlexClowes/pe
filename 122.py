from collections import deque


def sum_m(k_max):
    total = 0
    not_found = set(range(2, k_max + 1))
    q = deque()
    q.append(((1,), 0))
    while not_found:
        vals, depth = q.popleft()
        for val in vals:
            new_val = val + vals[-1]
            if new_val > k_max:
                break
            if new_val in not_found:
                not_found.remove(new_val)
                total += depth + 1
            if new_val < k_max:
                q.append((vals + (new_val,), depth + 1))
    return total


def main():
    print(sum_m(200))


if __name__ == "__main__":
    main()
