
'''
Print all elements from 1 to N*N
input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
'''


def printSpiral(N):
    # Initialize the 2D array with zeros
    arr = [[0]*N for _ in range(N)]
    
    # Define the four directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    # Initialize the current position and direction
    x, y, dir_idx = 0, 0, 0  # Start at arr[0][0], going right
    
    # Fill the array with numbers from 1 to N*N
    num = 1
    for _ in range(N*N):
        arr[x][y] = num
        num += 1
        
        # Move in the current direction
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy
        
        # Check if the move is valid (within bounds and not visited)
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            # Reverse direction
            dir_idx = (dir_idx + 1) % 4  # Cycle through the directions
            
            # Adjust position to continue in the new direction
            dx, dy = directions[dir_idx]
            nx, ny = x + dx, y + dy
            
            # Ensure the move is valid
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                x, y = nx, ny
                #print("AAAA")
            else:
                # If the move is invalid, backtrack to the last valid position
                #print("BBBB")
                #print(f"x is {x}, y is {y}")
                #print(f"nx is {nx}, ny is {ny}")
                #print(f"dx is {dx}, ny is {dy}")
                #print(f"arr[nx][ny] is {arr[nx][ny]}")
                
                x -= dx
                y -= dy
                
                
    # Print the array in spiral order
    for row in arr:
        print(row)

# Example usage
N = 3
printSpiral(N)