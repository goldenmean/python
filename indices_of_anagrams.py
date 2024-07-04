
'''
Given a string s and a string p, return all the starting indices of p’s anagrams within s.
Note: Both strings will contain at least one character and will only contain lowercase alphabetical characters.

Ex: Given the following s and p…

s = "abcbabc", p = "abc", return [0, 2, 4].
Ex: Given the following s and p…

s = "abc", p = "def", return [].
'''

def findAnagrams(s: str, p: str):
    # Initialize result list and character count dictionaries
    result = []
    if len(s) < len(p):
        return result
    
    # Initialize the character count dictionaries
    pCount, sCount = {}, {}
    
    # Count frequencies of each character in p
    for char in p:
        pCount[char] = pCount.get(char, 0) + 1
    
    # Initialize the window's character count
    for i in range(len(p)):
        sCount[s[i]] = sCount.get(s[i], 0) + 1
    
    # Compare counts at the start of the sliding window
    if sCount == pCount:
        result.append(0)
    
    # Slide the window across s, updating counts and checking for matches
    for i in range(len(p), len(s)):
        # Add the new character to the window's count
        sCount[s[i]] = sCount.get(s[i], 0) + 1
        # Remove the oldest character from the window's count
        sCount[s[i-len(p)]] -= 1
        if sCount[s[i-len(p)]] == 0:
            del sCount[s[i-len(p)]]
        # Compare counts and add index to result if they match
        if sCount == pCount:
            result.append(i - len(p) + 1)
    
    return result

# Example usage
print(findAnagrams("abcaabc", "abc"))
print(findAnagrams("abcbabc", "abc"))  # Output: [0, 2, 4]
print(findAnagrams("abc", "def"))  # Output: []



'''
def generate_anagrams(s):
    def backtrack(start=0):
        if start == len(s):
            result.append(''.join(s))
        for i in range(start, len(s)):
            # Swap characters at indices start and i
            s[start], s[i] = s[i], s[start]
            # Generate all permutations for the substring starting at start + 1
            backtrack(start + 1)
            # Swap back to revert the change to s
            s[start], s[i] = s[i], s[start]
    
    result = []
    s = list(s)  # Convert string to list for easier swapping
    backtrack()
    return result
'''