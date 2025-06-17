def is_safe(row, col, board, n):
    # Check upper direction
    for i in range(row):
        if board[i][col] == "Q":
            return False
    # Check left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r -= 1
        c -= 1
    # Check right diagonal
    r, c = row, col
    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False
        r -= 1
        c += 1
    return True

def solve_n_queens(no_queens, row, board, solutions):
    if row == no_queens:
        solution = []
        for r in board:
            row_str = "".join(r)
            solution.append(row_str)
        solutions.append(solution)
        return solutions

    for col in range(no_queens):
        if is_safe(row, col, board, no_queens):
            board[row][col] = "Q"  # Place queen
            solve_n_queens(no_queens, row + 1, board, solutions)  # Recur to place next queen
            board[row][col] = "."  # Backtrack

    return solutions

def n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]  # Create an n x n board
    solutions = []
    return solve_n_queens(n, 0, board, solutions)

# Example usage
no_queens = 8  # Change this to 12 for a 12x12 chessboard
solutions = n_queens(no_queens)
for solution in solutions:
    for row in solution:
        print(row)
    print()  # Print a blank line between solutions

            
    