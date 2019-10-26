from collections import defaultdict

import numpy as np


def get_data():
    with open("data/p082_matrix.txt") as f:
        data = [line.strip().split(",") for line in f]
    data = np.array(data).astype(np.int32)
    return data


def build_graph(size):
    graph = defaultdict(list)
    graph["start"] = [(i, 0) for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i > 0:
                graph[i, j].append((i - 1, j))
            if i < size - 1:
                graph[i, j].append((i + 1, j))
            if j < size - 1:
                graph[i, j].append((i, j + 1))
    return graph


def dijkstra(graph, weights):
    size = weights.shape[0]
    ends = [(i, size - 1) for i in range(size)]
    unvisited = {node: None for node in graph.keys()}
    visited = {}
    current = "start"
    current_dist = 0
    unvisited[current] = current_dist
    while True:
        for neighbour in graph[current]:
            if neighbour in unvisited:
                new_dist = current_dist + weights[neighbour]
                if unvisited[neighbour] is None or unvisited[neighbour] > new_dist:
                    unvisited[neighbour] = new_dist
        visited[current] = current_dist
        del unvisited[current]
        if all(end in visited for end in ends):
            return min(visited[end] for end in ends)
        candidates = [
            (node, dist) for node, dist in unvisited.items() if dist is not None
        ]
        current, current_dist = sorted(candidates, key=lambda x: x[1])[0]


def main():
    data = get_data()
    graph = build_graph(data.shape[0])
    print(dijkstra(graph, data))


if __name__ == "__main__":
    main()
