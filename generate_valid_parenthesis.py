'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

def generate_valid_parenthesis(n):
    result=[]

    def backtrack(s, open, close):
        print(s,open,close)
        if len(s) == 2*n:
            result.append(s)
            #print(s,open,close)
            return 
        
        if open < n:
            print("Before calling Left",s,open,close)
            #Add opening parenthesis
            backtrack(s + '(', open+1, close)

        if close < open:
            print("Before calling Right",s,open,close)
            #we can add closing parenthesis
            backtrack(s + ')', open, close+1)

    backtrack('', 0, 0)
    return result


n = 3
print(generate_valid_parenthesis(n))
