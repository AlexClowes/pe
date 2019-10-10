import numpy as np


def get_data_as_array(str_data):
    n_rows = len(str_data)
    data = np.zeros((n_rows, n_rows))
    for i in range(n_rows):
        for j, val in enumerate(map(int, str_data[i].split(" "))):
            data[i,j] = val
    return data


def get_max_path_val(data):
    max_vals = np.zeros_like(data, dtype=np.int32)
    max_vals[-1, :] = data[-1, :]
    for i in range(data.shape[0] - 2, -1, -1):
        for j in range(data.shape[0] - 1):
            max_vals[i, j] = data[i, j] + max(max_vals[i + 1, j], max_vals[i + 1, j + 1])
    return max_vals[0, 0]


def main():
    #data = get_data_as_array(str_data)
    with open("data/p067_triangle.txt") as f:
        data = [line for line in f]
    data = get_data_as_array(data)
    print(get_max_path_val(data))


if __name__ == "__main__":
    main()
