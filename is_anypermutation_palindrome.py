
'''
Given a string, s, return whether or not some permutation of s could form a palindrome.
Ex: Given the following string s…
s = "aeae", return true ("aeea" or "eaae").
Ex: Given the following string s…
s = "computer", return false.
'''
def can_form_palindrome(s):
    from collections import Counter

    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Count the number of characters that have an odd frequency
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    # A string can form a palindrome if at most one character has an odd frequency
    return odd_count <= 1

# Example usage
s1 = "aeae"
s2 = "computer"
print(can_form_palindrome(s1))  # Output: True
print(can_form_palindrome(s2))  # Output: False