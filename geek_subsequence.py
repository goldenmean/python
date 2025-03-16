
"""
Find if a given string has a subsequence(non-contiguous string as well)
that matches string "geek" 
"""


def hasGeekSubsequence(str : str) -> bool:
    t="geek"
    tidx = 0
    
    for c in str:
        if c == t[tidx]:
            tidx+=1
            if tidx == len(t):
                return True
    return False