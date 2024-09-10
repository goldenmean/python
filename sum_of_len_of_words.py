'''
Given an array of words and a string of characters, chars, return the sum of the lengths of words that can be formed using only the chars.
Note: Each character within chars can only be used once.

Ex: Given the following words and chars…

words = ["abc", "cab"], chars = "bac", return 6 ("abc"'s length + "cab"'s length).
'''
from collections import Counter

def sum_of_lengths(words, chars):
    
    ccnt = Counter(chars)
    reslen = 0    

    for i in range(len(words)):
        wcnt = Counter(words[i])
        brk = 0
        print(f"reslen is {reslen}")
        for k,v in wcnt.items():
            if k not in ccnt or v > ccnt[k]:
                print("break")
                brk = 1
                break
            else:
                pass

        if not brk:
            reslen += len(words[i])
        
    return reslen


words = ["abc", "cab"]; chars = "bac"
print(sum_of_lengths(words, chars))