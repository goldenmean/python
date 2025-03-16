"""
Given a string of parentheses, find the balanced string that can be 
produced from it using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", 
you could return "()()()()".
"""
# Note: the total number of operations is the same whether we use insertions,
# deletions, or a combination of both
# Below code only uses insertions to balance the parentheses

def balance_parentheses(s):
    """
    Balance a string of parentheses using minimum insertions and deletions.
    
    Args:
        s: String of parentheses
    
    Returns:
        A balanced string of parentheses
    """
    # Stack to keep track of opening parentheses
    stack = []
    # String to build the balanced result
    result = []
    
    # First pass: handle closing parentheses without matching opening ones
    for char in s:
        if char == '(':
            stack.append(char)
            result.append(char)
        elif char == ')':
            if stack:  # If there's a matching opening parenthesis
                stack.pop()
                result.append(char)
            else:  # No matching opening parenthesis, insert one
                result.append('(')
                result.append(char)
    
    # Second pass: handle remaining opening parentheses without matching closing ones
    if stack:
        # Add closing parentheses for each unmatched opening parenthesis
        result.extend([')'] * len(stack))
    
    return ''.join(result)

# Test cases
print(balance_parentheses("(()"))    # Output: "(())"
print(balance_parentheses("))()("))  # Output: "()()()()"