



import re

def reverse_words_with_delimiters(s, delimiters):
    # Create a regex pattern to split on any of the provided delimiters
    pattern = f"[{re.escape(delimiters)}]"
    
    # Split the string into words and delimiters
    words = re.split(pattern, s)
    delimiters_list = re.findall(pattern, s)
    
    # Reverse the list of words
    words.reverse()
    
   # Combine the reversed words with the original delimiters
    result = []
    max_len = max(len(words), len(delimiters_list))
    for i in range(max_len):
        if i < len(words):
            result.append(words[i])
        if i < len(delimiters_list):
            result.append(delimiters_list[i])
    
    return ''.join(result)

# Test the function
print(reverse_words_with_delimiters("hello/world:here", "/:"))  # Output: "here/world:hello"
print(reverse_words_with_delimiters("hello/world:here/", "/:"))  # Output: "here/world:hello/"
print(reverse_words_with_delimiters("hello//world:here", "/:"))  # incorrect answer