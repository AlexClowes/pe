from collections import defaultdict


def load_graph():
    with open("data/p107_network.txt") as f:
        graph = defaultdict(dict)
        for v1, line in enumerate(f):
            for v2, weight in enumerate(line.strip().split(",")):
                if weight != "-":
                    graph[v1][v2] = int(weight)
    return graph


def total_weight(graph):
    total = 0
    for vertex, edges in graph.items():
        for weight in edges.values():
            total += weight
    return total // 2


def min_spanning_tree_weight(graph):
    first_vertex = next(iter(graph))
    tree_vertices = {first_vertex}
    tree_weight = 0
    while len(tree_vertices) < len(graph):
        min_weight = float("inf")
        for v1 in tree_vertices:
            for v2 in graph[v1]:
                if v2 not in tree_vertices and graph[v1][v2] < min_weight:
                    min_weight = graph[v1][v2]
                    new_vertex = v2
        tree_vertices.add(new_vertex)
        tree_weight += min_weight
    return tree_weight


def main():
    graph = load_graph()
    print(total_weight(graph) - min_spanning_tree_weight(graph))


if __name__ == "__main__":
    main()
