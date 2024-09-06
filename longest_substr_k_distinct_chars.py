'''
You are given a string s, and an integer k. Return the length of the longest substring in s that
contains at most k distinct characters.

For instance, given the string: aabcdefff and k = 3, then the longest substring with 3 distinct 
characters would be defff. The answer should be 5.
'''

def longest_substring_with_k_distinct(s, k):
    if k == 0 or not s:
        return 0
    
    left = 0
    max_length = 0
    char_count = {}

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "aabcdefff"
k = 3
print(longest_substring_with_k_distinct(s, k))  # Output: 5