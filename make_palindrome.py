'''
Given a string, s, which consists of only lowercase alphabetical characters,
return the length of the longest palindrome you can form using its letters.

Ex: Given the following s...
s = “aa”, return 2.

Ex: Given the following s...
s = “abbcaadabac”, return 9.
'''
from collections import Counter

def make_palindrome(s):
    d = Counter(s)

    res = 0
    
    if len(d) == 1:
        return len(s)

    for v in d.values():
        if v == 1:
            res += 1
        else:
            res += v // 2 * 2 
                
    return res

#print(make_palindrome("abbcaadabac"))
#print(make_palindrome("aaab"))
print(make_palindrome("aaa"))
