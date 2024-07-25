
'''
The player can jump on any position having a number 0 , but cannot jump to a 
position having 1 Determine the minimum number of jumps it will take to jump
from the starting postion to the last position. It is always possible to win
the game. There will be a 0 value at first poistion and last in the array.

You will get an input array as below C = [0,1,0,0,0,1,0] The player can jump
from its current location by 1 or 2 steps.

The player must avoid the indices 1 and 5. They could follow these two paths
to reach to end location  :0 --> 2 -->4 -->6  or 0 -->2 -->3 --> -->6 . 
The first path takes 3 jumps while the second takes 4.  You should return 
minimum number of jumps needed , so Return 3
'''



from collections import deque

def min_jumps(C):
    n = len(C)
    if n == 0:
        return 0

    # Initialize the queue with the starting position (index 0) and 0 jumps
    queue = deque([(0, 0)]) #(index of current position in the array, jumps needed to reach there)
    visited = set()
    visited.add(0)

    #BFS algorithm - we check which all positions we can jump to from current and queue them if valid
    while queue:
        current, jumps = queue.popleft()
        print(f"current is {current} and jumps is {jumps}")

        # Check if we have reached the last position
        if current == n - 1:
            print(queue)
            return jumps            

        # Try to jump to current + 2
        if current + 2 < n and C[current + 2] == 0 and (current + 2) not in visited:
            queue.append((current + 2, jumps + 1))
            visited.add(current + 2)

        # Try to jump to current + 1 
        if current + 1 < n and C[current + 1] == 0 and (current + 1) not in visited:
            queue.append((current + 1, jumps + 1))
            visited.add(current + 1)

        
            
        print(f"queue is {queue}")
        
 
    return -1  # Should never reach here since it's always possible to win the game

# Example usage
#C = [0, 1, 0, 0, 0, 1, 0]
#C = [0, 0, 0, 0, 0]
#C = [0, 0, 1, 0, 0, 1, 0]
#C = [0, 0, 0, 0, 1, 0]

print(min_jumps(C))  