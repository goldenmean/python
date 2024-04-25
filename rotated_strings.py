'''
Rotated strings 

Given two strings A and B, return whether or not A can be shifted some number of times to get B. 
For example, if A is abcde and B is cdeab, return true. 
If A is abc and B is acb, return false. 
'''

def rotated_strings(s1, s2):
    if len(s1)!=len(s2):
        return False
    
    if s1 == s2:
        return True
    
    l=s1[0]
    r=0
    for i in range(1,len(s2)):
        news = s2[i:]+s2[:i]
        if news == s1:
            return True
    return False


# s1 = "abcde" 
# s2 = "cdeab"
# s1 = "cbcde" 
# s2 = "cdecb"
s1 = "abc" 
s2 = "acb"

res=rotated_strings(s1,s2)
print("Strings are rotated") if res else print("Strings different")
