import numpy as np


str_data = (
    "75",
    "95 64",
    "17 47 82",
    "18 35 87 10",
    "20 04 82 47 65",
    "19 01 23 75 03 34",
    "88 02 77 73 07 63 67",
    "99 65 04 28 06 16 70 92",
    "41 41 26 56 83 40 80 70 33",
    "41 48 72 33 47 32 37 16 94 29",
    "53 71 44 65 25 43 91 52 97 51 14",
    "70 11 33 28 77 73 17 78 39 68 17 57",
    "91 71 52 38 17 14 91 43 58 50 27 29 48",
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23",
)


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
    data = get_data_as_array(str_data)
    print(get_max_path_val(data))


if __name__ == "__main__":
    main()
