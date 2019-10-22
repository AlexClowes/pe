from datetime import date


def main():
    total = sum(
        date(year, month, 1).weekday() == 6
        for year in range(1901, 2001)
        for month in range(1, 13)
    )
    print(total)


if __name__ == "__main__":
    main()
