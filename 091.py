from itertools import product


def triangle_count(n):
    count = n * n
    p_coords = list(product(range(n + 1), repeat=2))
    q_coords = list(product(range(n + 1), repeat=2))
    for xp, yp in p_coords:
        for xq, yq in q_coords:
            if xp * yq == xq * yp:
                continue
            if yp * (yq - yp) == xp * (xp - xq):
                count += 1
    return count


def main():
    print(triangle_count(50))


if __name__ == "__main__":
    main()
