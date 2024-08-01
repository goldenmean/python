
'''
Given string of words, return the duplicate word from the stringFor example,
given 'The dog is the best', returns ["the"].
Likewise, given 'Happy thanksgiving, I am so full', you would return an empty
array. This is because there are no duplicates in the string
'''


def find_duplicate_words(s):
    # Convert the string to lowercase and split into words
    words = s.lower().split()
    
    # Use a dictionary to count occurrences of each word
    word_count = {}
    for word in words:
        word = word.strip(",.!?")  # Remove punctuation
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Collect words that appear more than once
    duplicates = [word for word, count in word_count.items() if count > 1]
    
    return duplicates

# Example usage:
print(find_duplicate_words('The dog is the best'))  # Output: ['the']
print(find_duplicate_words('Happy thanksgiving, I am so full'))  # Output: []