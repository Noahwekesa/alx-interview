#!/usr/bin/python3
"""N queens puzzle"""

import sys


def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    # Check for queens in the same row
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check for queens in diagonals
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    """Solves the N-Queens problem using backtracking."""
    if col >= len(board):
        for row in board:
            for queen in row:
                print(queen, end=" ")
            print()
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1)
            board[i][col] = 0  # Backtrack


def n_queens(n):
    """Main function to handle user input and solve the puzzle."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = int(sys.argv[1])
    n_queens(n)
