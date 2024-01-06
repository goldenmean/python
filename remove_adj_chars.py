'''
This question is asked by Facebook. Given a string s containing only lowercase letters, 
continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
'''

def rem_adj_chars(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
            
            
            
            
#s = "abccba"
#s = "foobar"
#s = "babccbab"
s = "abccbefggfe"
s = "a!j!i!!t"
rem_adj_chars(s)    
print(rem_adj_chars(s))