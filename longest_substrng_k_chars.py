'''
https://mail.google.com/mail/u/0/#search/label%3Aunread+the+daily+byte/FMfcgzQVwnWTnRSkbhgKqdmxFdSXMPss
Given a string s and a value k, return the length of the longest substring that
contains at most k distinct character.

Ex: Given the following string s and integer k...

s = "abccccd", k = 3, return 6 (“abcccc” is length 6).
Ex: Given the following string s and integer k...

s = "rrr", k = 1, return 3.

'''

def longest_substring_with_k_distinct_chars(s, k):
    if k == 0:
        return 0

    char_freq = {}
    max_length = 0
    #Sliding window algorithm - left and right pointers for the window
    left, right = 0, 0

    while right < len(s):
        # Increment the frequency of the current character
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1
        
        # If we have already seen more than k distinct characters, we need to shrink the window
        while len(char_freq) > k:
            # Decrement the frequency of the leftmost character
            char_freq[s[left]] -= 1
            # If the frequency of the leftmost character is 0, we need to remove it
            if char_freq[s[left]] == 0:
                # Remove the leftmost character
                del char_freq[s[left]]
            # Move the left pointer forward
            left += 1
        # Update the maximum length - this is the length of the longest substring with k distinct characters
        max_length = max(max_length, right - left + 1)
        # Move the right pointer forward
        right += 1
    # Return the maximum length
    return max_length

# Test cases
print(longest_substring_with_k_distinct_chars("abccccd", 3)) # Output: 6
print(longest_substring_with_k_distinct_chars("rrr", 1)) # Output: 3
print(longest_substring_with_k_distinct_chars("abccccdd", 3)) 
print(longest_substring_with_k_distinct_chars("bcccc", 3))

 
        
