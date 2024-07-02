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
    odd_count = 0  # Count how many characters appear an odd number of times

    for v in d.values():
        if v % 2 == 0:
            res += v
        else:
            odd_count += 1
            res += v - 1  # Add the even part of the count

    # Allow one odd character (if any) to be in the middle
    if odd_count > 0:
        res += 1

    return res


#print(make_palindrome("abbcaadabac"))
#print(make_palindrome("aaab"))
#print(make_palindrome("aaa"))
#print(make_palindrome("abc")) #should be 1
print(make_palindrome("aabc")) #should be 1

