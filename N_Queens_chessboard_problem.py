r"""
N-Queens Problem
The N-Queens problem is a classic problem in computer science and mathematics.
The goal is to place N queens on an N×N chessboard such that no two queens
threaten each other. A queen can attack any other piece that is on the same
row, column, or diagonal.
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

#Below solution gives first solution and not all possible solutions. it stops after 1st 
#This function returns True if queen can be placed at location i,j else it returns False
def recursive_n_queens(board, col, N):
    if col >= N:  # All queens have been placed
        return True
    
    for i in range(N):
        if not is_attacked(i, col, board, N):
            board[i][col] = 1  # Place current queen at cell (i,col)
            if recursive_n_queens(board, col + 1, N): # recursively place next queen at col+1 
                return True  # If solution is found return True
            board[i][col] = 0  # If solution is not found, remove current queen from (i,col)
    
    return False

def is_n_queens_possible(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if recursive_n_queens(board, 0, N): # Start placing queens from col 0
        return board
    else:
        return None

# Example usage
N = 4
solution = is_n_queens_possible(N)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists")
