'''
Given a string, s, return the length of the longest substring between two characters that are equal.
Note: s will only contain lowercase alphabetical characters.

Ex: Given the following string s…

s = "bbccb", return 3 ("bcc" is length 3).
Ex: Given the following string s…

s = "abb", return 0.
'''

def longest_substring_between_equal_chars(s):
    first_occurrence = {}
    max_length = 0

    for i, char in enumerate(s):
        if char in first_occurrence:
            # Calculate the length of the substring between two equal characters
            length = i - first_occurrence[char] - 1
            max_length = max(max_length, length)
        else:
            # Store the first occurrence of the character
            first_occurrence[char] = i

    return max_length

# Example usage:
s1 = "bbccb"
s2 = "abb"

print(longest_substring_between_equal_chars(s1))  # Output: 3
print(longest_substring_between_equal_chars(s2))  # Output: 0