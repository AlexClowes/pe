from math import sqrt


def next_point(x0, y0, x1, y1, eps=1e-6):
    m0 = (y1 - y0) / (x1 - x0)
    m1 = -4 * x1 / y1
    t = (m0 - m1) / (1 + m0 * m1)
    m2 = (m1 - t) / (1 + m1 * t)
    c = y1 - m2 * x1
    x2 = (-c * m2 + sqrt(400 + 100 * m2 * m2 - 4 * c * c)) / (4 + m2 * m2)
    if abs(x1 - x2) < eps:
        x2 = (-c * m2 - sqrt(400 + 100 * m2 * m2 - 4 * c * c)) / (4 + m2 * m2)
    y2 = m2 * x2 + c
    return x2, y2


def main():
    x0, y0 = 0.0, 10.1
    x1, y1 = 1.4, -9.6
    count = 0
    while abs(x1) > 0.01 or y1 < 0:
        x0, y0, x1, y1 = x1, y1, *next_point(x0, y0, x1, y1)
        count += 1
    print(count)


if __name__ == "__main__":
    main()
