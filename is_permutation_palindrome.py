
'''
Given a string, determine whether any permutation of it is a palindrome.

For example, "carrace" should return true, since it can be rearranged to form
 racecar, which is a palindrome. 
 "daily" should return false, since there's no rearrangement that can form a palindrome

'''
import itertools
def is_permutation_palindrome(s):
    p=list(itertools.permutations(s))

    for i in p:
        if list(i)==list(i)[::-1]:
            return True

    return False


#s="carrace"
#s="ajit"
s="daily"
print(is_permutation_palindrome(s))




