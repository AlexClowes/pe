import numpy as np


def get_data():
    with open("data/p081_matrix.txt") as f:
        data = [line.strip().split(",") for line in f]
    data = np.array(data).astype(np.int32)
    return data


def minimal_path_sum(data):
    min_vals = np.zeros_like(data)
    min_vals[0, :] = np.cumsum(data[0, :])
    min_vals[:, 0] = np.cumsum(data[:, 0])
    for i in range(1, data.shape[0]):
        for j in range(1, data.shape[1]):
            min_vals[i, j] = data[i, j] + min(min_vals[i - 1, j], min_vals[i, j - 1])
    return min_vals[-1, -1]
    

def main():
    data = get_data()
    print(minimal_path_sum(data))


if __name__ == "__main__":
    main()
