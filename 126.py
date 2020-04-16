from itertools import count


def layer_size(x, y, z, n):
    return 2 * (x * y + y * z + z * x) + 4 * (n - 1) * (x + y + z) + 4 * (n - 1) * (n - 2)


def main():
    C = [0] * 20000
    for x in count(1):
        for y in count(x):
            for z in count(y):
                for n in count(1):
                    size = layer_size(x, y, z, n)
                    if size >= 20000:
                        break
                    C[size] += 1
                if n == 1:
                    break
            if z == y:
                break
        if y == x:
            break

    for i in range(20000):
        if C[i] == 1000:
            print(i)
            break


if __name__ == "__main__":
    main()
