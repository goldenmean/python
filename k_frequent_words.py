"""
Given a non-empty list of words, return the k most frequent words. The output 
should be sorted from highest to lowest frequency, and if two words have the
same frequency, the word with lower alphabetical order comes first. 
Input will contain only lower-case letters.

Example:

Input: ["daily", "interview", "pro", "pro", 
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
"""

from collections import Counter
from typing import List

def top_k_frequent_words(words: List[str], k: int) -> List[str]:
    # Step 1: Count the frequency of each word
    word_count = Counter(words)
    
    # Step 2: Sort the words first by frequency (in descending order) and then alphabetically
    sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], word))
    
    # Step 3: Return the top k words
    return sorted_words[:k]

# Example usage
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(top_k_frequent_words(words, k))