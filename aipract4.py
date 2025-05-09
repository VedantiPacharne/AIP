def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Track columns and diagonals to implement branch and bound
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # "/" diagonals
    diag2 = [False] * (2 * n - 1)  # "\" diagonals
    
    solutions = []

    def backtrack(row):
        if row == n:
            # A valid solution is found
            solution = [row[:] for row in board]
            solutions.append(solution)
            return
        
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                # Place queen
                board[row][col] = 1
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                
                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row][col] = 0
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    backtrack(0)
    return solutions


# Test for N = 4
n = 4
result = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(result)}\n")
for sol in result:
    print_solution(sol)
