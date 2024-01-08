'''
This question is asked by Amazon. Given two strings s and t, which represents a sequence of keystrokes, 
where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
'''

def backspace_keypress(s,t):
    stk1 = []
    stk2 = []
    for c in s:
        if c != "#":
            stk1.append(c)
        else:
            stk1.pop()
    
    for c in t:
        if c != "#":
            stk2.append(c)
        else:
            stk2.pop()
    
    print(stk1, stk2)
    return stk1 == stk2

#s = "ABC#"
#t = "CD##AB"

s = "cof#dim#ng"
t = "code"

#s = "como#pur#ter"
#t = "computer"

print(backspace_keypress(s,t))