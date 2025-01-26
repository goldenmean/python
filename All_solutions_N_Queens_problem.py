"""
Give all possible solutions of N queens problem 
"""
def is_attacked(x, y, board, N):
    if any(board[x]):
        return True
    #if 1 in board[x]:
    #    return True
   
    if any(row[y] for row in board):
         return True
    #if 1 in [board[i][y] for i in range(N)]:
    #    return True
    
    for i in range(N):
        for j in range(N):
            if (i+j == x+y) or (i-j == x-y):
                if board[i][j]:
                    return True
    return False

def print_solution(board):
    for row in board:
        print(row)
    print()

def recursive_n_queens(board, col, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])
        return
    
    for i in range(N):
        if not is_attacked(i, col, board, N):
            board[i][col] = 1
            recursive_n_queens(board, col + 1, N, solutions)
            board[i][col] = 0

def find_all_solutions(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    recursive_n_queens(board, 0, N, solutions)
    return solutions

# Example usage
N = 4
all_solutions = find_all_solutions(N)
print(f"Found {len(all_solutions)} solutions:")
for i, solution in enumerate(all_solutions, 1):
    print(f"Solution {i}:")
    print_solution(solution)