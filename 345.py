import numpy as np


def matrix_sum(matrix):
    N = matrix.shape[0]

    memo = {}
    def dfs(unoccupied_rows):
        if unoccupied_rows not in memo:
            # Base case
            if len(unoccupied_rows) == 1:
                return matrix[unoccupied_rows[0], -1]

            col = N - len(unoccupied_rows)
            best_sum = 0
            for row in unoccupied_rows:
                new_unoccupied_rows = tuple(set(unoccupied_rows) - {row})
                best_sum = max(best_sum, matrix[row, col] + dfs(new_unoccupied_rows))
            memo[unoccupied_rows] = best_sum
        return memo[unoccupied_rows]

    return dfs(tuple(range(N)))


def main():
    with open("data/p345_matrix.txt") as f:
        matrix = np.array([[int(n) for n in line.split()] for line in f])
    print(matrix_sum(matrix))


if __name__ == "__main__":
    main()
