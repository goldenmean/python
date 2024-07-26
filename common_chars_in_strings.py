'''
Given a string array, words, return a list containing all the characters that are 
common to all the words.
Note: If a character appears multiple times in all the words it should also appear
 multiple times in your return list.

Ex: Given the following words…

words = ["abc", "ab", "a"], return ["a"].
Ex: Given the following words…

words = ["deef", "ddabee", "eebhk"], return ["e","e"].

'''

from collections import Counter

def common_chars(words):
    # Initialize the counter with the characters of the first word
    common_count = Counter(words[0])
    print(f"common_count dictionary is {common_count}")
    
    # Intersect the counter with characters of the remaining words
    for word in words[1:]:
        print(f"{Counter(word)}")
        common_count &= Counter(word)
    
    # Convert the counter to a list of characters
    result = list(common_count.elements())
    
    return result

# Examples
words1 = ["abc", "ab", "a"]
print(common_chars(words1))  # Output: ['a']

words2 = ["deef", "ddabee", "eebhk"]
print(common_chars(words2))  # Output: ['e', 'e']