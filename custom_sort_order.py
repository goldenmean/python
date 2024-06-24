'''
We are given two strings order and str, with the string order already sorted in a custom order.
Permute the characters of str such that they match the custom order in which order is sorted.
More specifically, if a character x occurs before a character y in order, then x should occur
before y in the permuted string e.g. order = 'fed' str = 'adef' output string should be = "feda"

'''


from collections import Counter

def customSort(order, str):
    # Count the occurrences of each character in 'str'
    str_count = Counter(str)
    
    # Initialize the result string
    result = []
    
    # Add characters present in 'order' to the result
    for char in order:
        if char in str_count:
            result.append(char * str_count.pop(char))
    
    # Add the remaining characters in str that were not in 'order'
    for char, count in str_count.items():
        result.append(char * count)
    
    return ''.join(result)

# Example usage:
#order = 'fed'; str = 'adef'
order = 'def'; str = 'adef'
output = customSort(order, str)
print(output)  # Output should be "feda"