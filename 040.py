def get_nth_digit(n):
    if n < 10:
        return n
    # Find correct block of numbers
    block_no = 1
    block_start_pos = 0
    block_end_pos = 9
    while n > block_end_pos:
        block_no += 1
        block_start_pos = block_end_pos + 1
        block_end_pos += (10 ** block_no - 10 ** (block_no - 1)) * block_no
    # Find number within block
    number = (n - block_start_pos) // block_no + 10 ** (block_no - 1)
    # Get digit within number
    return int(str(number)[(n - block_start_pos) % block_no])


def main():
    prod = 1
    for i in range(7):
        prod *= get_nth_digit(10**i)
    print(prod)


if __name__ == "__main__":
    main()
