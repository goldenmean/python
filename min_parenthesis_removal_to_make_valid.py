'''
Given a string s, remove the minimum number of parentheses to make s valid. 
Return all possible results.

Ex: Given the following string s...

s = "(()()()", return ["()()()","(())()","(()())"].
Ex: Given the following string s...

s = "()()()", return ["()()()"]
'''


def removeInvalidParentheses(s):
    def isValid(s):
        # Function to check if the parentheses string is valid
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0

    def backtrack(start, l_removed, r_removed, s):
        # If we have removed the minimum number of parentheses and s is valid
        if l_removed == 0 and r_removed == 0:
            if isValid(s):
                valid_expressions.add(s)
            return
        
        for i in range(start, len(s)):
            # To avoid duplicates, we only remove the first parentheses if there are no consecutive ones
            if i != start and s[i] == s[i - 1]:
                continue
            
            # If it's possible to remove a left parenthesis
            if l_removed > 0 and s[i] == '(':
                backtrack(i, l_removed - 1, r_removed, s[:i] + s[i+1:])
            
            # If it's possible to remove a right parenthesis
            if r_removed > 0 and s[i] == ')':
                backtrack(i, l_removed, r_removed - 1, s[:i] + s[i+1:])
    
    # Initial number of parentheses to be removed to make the string valid
    l_removed, r_removed = 0, 0
    for char in s:
        if char == '(':
            l_removed += 1
        elif char == ')':
            if l_removed == 0:
                r_removed += 1
            else:
                l_removed -= 1

    valid_expressions = set()
    backtrack(0, l_removed, r_removed, s)
    return list(valid_expressions)

# Example usage:
print(removeInvalidParentheses("(()()()"))
print(removeInvalidParentheses("()()()"))