#!/usr/bin/env python3
import sys


def parse_puzzle():
    puzzle = sys.stdin.read().strip().replace("\n", "").replace(" ", "")
    # Normalize different symbols for empty spots to '0'
    puzzle = puzzle.replace(".", "0").replace("?", "0").replace("*", "0")
    return puzzle


def index_to_var(i, j, k):
    """Converts Sudoku cell indices and value to a variable number for CNF."""
    return 81 * (i - 1) + 9 * (j - 1) + k


def generate_cnf(puzzle):
    clauses = []
    # Each cell contains at least one number
    for i in range(1, 10):
        for j in range(1, 10):
            clauses.append([index_to_var(i, j, k) for k in range(1, 10)])

    # Uniqueness in Rows
    for k in range(1, 10):
        for i in range(1, 10):
            for j in range(1, 9):
                for l in range(j + 1, 10):
                    clauses.append([-index_to_var(i, j, k), -index_to_var(i, l, k)])

    # Uniqueness in Columns
    for k in range(1, 10):
        for j in range(1, 10):
            for i in range(1, 9):
                for l in range(i + 1, 10):
                    clauses.append([-index_to_var(i, j, k), -index_to_var(l, j, k)])

    # Uniqueness in 3x3 Subgrids
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for i in range(1, 4):
                    for j in range(1, 4):
                        for l in range(i, 4):
                            for m in range(j + 1 if i == l else 1, 4):
                                x1 = index_to_var(3 * a + i, 3 * b + j, k)
                                x2 = index_to_var(3 * a + l, 3 * b + m, k)
                                clauses.append([-x1, -x2])

    # Encode pre-filled cells from the puzzle
    for i in range(9):
        for j in range(9):
            digit = puzzle[i * 9 + j]
            if digit.isdigit() and digit != "0":
                clauses.append([index_to_var(i + 1, j + 1, int(digit))])

    return clauses


def output_dimacs(clauses):
    variables = 9 * 9 * 9  # Total number of variables
    print(f"p cnf {variables} {len(clauses)}")
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")


def main():
    puzzle = parse_puzzle()
    clauses = generate_cnf(puzzle)
    output_dimacs(clauses)


if __name__ == "__main__":
    main()
