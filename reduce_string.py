"""
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

Example.

s=
"aab" shortens to b in one operation: remove the adjacent a characters.

s="abba"
Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.

s="aaabccddd" , output: "abd" 
"""
def reduce_string(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    result = ''.join(stack)
    return result if result else "Empty String"

# Test cases
print(reduce_string("aab"))        # Output: b
print(reduce_string("abba"))       # Output: Empty String
print(reduce_string("aaabccddd"))  # Output: abd