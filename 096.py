import numpy as np


def sudoku_gen():
    with open("data/p096_sudoku.txt") as f:
        f.readline()
        sudoku = np.zeros((9, 9), dtype=np.int32)
        for idx, line in enumerate(f, 1):
            if idx % 10 == 0:
                yield sudoku
            else:
                vals = list(map(int, line.strip()))
                sudoku[idx % 10 - 1, :] = vals
        yield sudoku


def find_empty_square(sudoku, start_search):
    i = start_search[0]
    for j in range(start_search[1], 9):
        if sudoku[i, j] == 0:
            return i, j
    for i in range(start_search[0] + 1, 9):
        for j in range(9):
            if sudoku[i, j] == 0:
                return i, j
    return None


def is_valid(sudoku, row, col, num):
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    return (
        num not in sudoku[row, :]
        and num not in sudoku[:, col]
        and num not in sudoku[box_row : box_row + 3, box_col : box_col + 3]
    )


def solve(sudoku, start_search=(0,0)):
    empty_square = find_empty_square(sudoku, start_search)
    if not empty_square:
        return True
    for n in range(1, 10):
        if is_valid(sudoku, *empty_square, n):
            sudoku[empty_square[0], empty_square[1]] = n
            if solve(sudoku, start_search=empty_square):
                return True
            sudoku[empty_square[0], empty_square[1]] = 0
    return False


def main():
    total = 0
    for sudoku in sudoku_gen():
        solve(sudoku)
        total += 100 * sudoku[0, 0] + 10 * sudoku[0, 1] + sudoku[0, 2]
    print(total)


if __name__ == "__main__":
    main()
