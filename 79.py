def get_passcodes():
    with open("data/p079_keylog.txt") as f:
        return sorted({line.strip() for line in f})


def main():
    print("By hand -> 73162890")


if __name__ == "__main__":
    main()
