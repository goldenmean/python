"""
You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd

"""

def smallest_string_after_moves(s, k):
    n = len(s)
    if k == 1:
        return min(s[i:] + s[:i] for i in range(n))
    
    # If k > 1, we can always achieve the lexicographically smallest string
    return ''.join(sorted(s))

# Test cases
print(smallest_string_after_moves("daily", 1))  # Output: "ailyd"
print(smallest_string_after_moves("cba", 1))    # Output: "acb"
print(smallest_string_after_moves("dcba", 2))   # Output: "abcd"