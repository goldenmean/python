'''
There are N prisoners standing in a circle, waiting to be executed. The executions are 
carried out starting with the kth person, and removing every successive kth person going
in clockwise direction until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to
be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3

This is Josephus problem


'''

def josephus(N, k):
    if N == 1:
        return 0
    else:
        print(f"N = {N}, k = {k}")
        retval= (josephus(N - 1, k) + k) % N
        print(f"N = {N}, retval = {retval}")
        return retval

def find_survivor(N, k):
    # Convert the 0-based index to a 1-based index
    return josephus(N, k) + 1

# Example usage:
N = 5; k = 2
#N = 2; k = 2
#N=41; k = 3
print(f"Last survivor: {find_survivor(N, k)}") 