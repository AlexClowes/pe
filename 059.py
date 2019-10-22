from itertools import product, cycle


def decode(encrypted_text, password):
    encrypted_text = map(int, encrypted_text)
    return "".join(chr(n ^ ord(p)) for n, p in zip(encrypted_text, cycle(password)))


def main():
    with open("data/p059_cipher.txt") as f:
        encrypted_text = f.read().strip().split(",")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = ("".join(tup) for tup in product(alphabet, repeat=3))
    for p in passwords:
        text = decode(encrypted_text, p)
        if "the" in text and "and" in text and "have" in text:
            break
    print(sum(ord(char) for char in text))


if __name__ == "__main__":
    main()
