from collections import deque
from itertools import combinations_with_replacement, permutations
from operator import add, sub, mul, truediv


operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def eval_rpn(expr):
    stack = deque()
    for el in expr:
        if el in operators:
            sec = stack.pop()
            fst = stack.pop()
            el = operators[el](fst, sec)
        stack.append(el)
    return stack.pop()


def valid_rpn(expr):
    num_count = 0
    op_count = 0
    for el in expr:
        if el in operators:
            op_count += 1
            if op_count > num_count - 1:
                return False
        else:
            num_count += 1
    return True


def seq_length(a, b, c, d):
    vals = set()
    for ops in combinations_with_replacement(operators, 3):
        for expr in permutations((a, b, c, d) + ops):
            if valid_rpn(expr):
                try:
                    vals.add(eval_rpn(expr))
                except ZeroDivisionError:
                    pass
    n = 1
    while n in vals:
        n += 1
    return n - 1


def main():
    longest_seq = 0
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    seq_len = seq_length(a, b, c, d)
                    if seq_len > longest_seq:
                        longest_seq = seq_len
                        best_vals = (a, b, c, d)
    print(*best_vals, sep="")


if __name__ == "__main__":
    main()
