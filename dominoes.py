'''
You’re given a set of integers, dominoes, that represent a set of domino tiles.
The value of domino represents either weight and its sign, positive or negative,
represents the direction it is falling: positive falls right and negative
falls left. When two dominoes collide, the larger domino destroys the smaller
domino. If two dominoes of the same size collide, both dominoes are destroyed.
After all the collisions, return the state of the dominoes.

Ex: Given the following dominoes…

dominoes = [3, -3], return [].
Ex: Given the following dominoes…

dominoes = [1, 2, -3, 2, -1], return [-3, 2] (-3 destroys both dominoes to its
left and the second two destroys the domino to the right of it).
'''

def domino_collision(dominoes):
    stack = []
    for domino in dominoes:
        print(domino)
        # Collision logic
        while stack and stack[-1] > 0 and domino < 0:
            # If the incoming left-falling domino is bigger, it destroys the right-falling one
            if abs(stack[-1]) < abs(domino):
                stack.pop()
                print(f"A, {stack}")
                if not stack or stack[-1] < 0:                    
                    stack.append(domino)
                    print(f"B, {stack}")
                    break
            # If they are of the same size, destroy both
            elif abs(stack[-1]) == abs(domino):
                #remove the previous smaller domino and do not add the current domino to stack
                stack.pop()
                print(f"C, {stack}")
                break
            else:
                print(f"D, {stack}")
                #Don't add the current domino to stack
                break
        else:            
            stack.append(domino)
            print(f"E, {stack}")

    return stack

# Example usage
dominoes1 = [3, -3]
#dominoes2 = [1, 2, -3, 2, -1]
print(domino_collision(dominoes1))  # Output: []
#print(domino_collision(dominoes2))  # Output: [-3, 2]