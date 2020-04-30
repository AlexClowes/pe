from itertools import product


def build_graph(n):
    return {node: (node[1:] + (0,), node[1:] + (1,)) for node in product((0, 1), repeat=n)}


def path_to_int(path):
    ret = 0
    for node in path:
        ret *= 2
        ret += node[0]
    return ret


def get_hamiltonian_paths(graph, start):
    def f(path):
        if len(path) == len(graph):
            yield path
        current_node = path[-1]
        for next_node in graph[current_node]:
            if next_node not in path:
                yield from f(path + (next_node,))

    yield from f((start,))


def sum_de_bruijn_sequences(n):
    hamiltonian_paths = get_hamiltonian_paths(build_graph(n), (0,) * n)
    return sum(path_to_int(path) for path in hamiltonian_paths)


def main():
    print(sum_de_bruijn_sequences(5))


if __name__ == "__main__":
    main()
