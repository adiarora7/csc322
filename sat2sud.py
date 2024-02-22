#!/usr/bin/env python3
import sys

def var_to_index(var):
    """Converts a variable number back to Sudoku cell indices and value."""
    var -= 1  # Adjust for 1-based indexing
    k = var % 9 + 1
    j = (var // 9) % 9 + 1
    i = var // 81 + 1
    return (i, j, k)

def parse_solution():
    lines = sys.stdin.readlines()
    solution = []
    for line in lines:
        if line.strip().startswith('SAT'):
            continue  # Skip the SAT status line
        solution.extend(line.strip().split())
    # Filter out only positive integers (True variables)
    positive_vars = [int(var) for var in solution if var.isdigit() and int(var) > 0]
    return positive_vars


def fill_sudoku(positive_vars):
    grid = [['0' for _ in range(9)] for _ in range(9)]
    for var in positive_vars:
        i, j, k = var_to_index(var)
        grid[i-1][j-1] = str(k)
    return grid

def output_sudoku(grid):
    for row in grid:
        print(' '.join(row))

def main():
    positive_vars = parse_solution()
    grid = fill_sudoku(positive_vars)
    output_sudoku(grid)

if __name__ == "__main__":
    main()
