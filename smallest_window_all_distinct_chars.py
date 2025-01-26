"""
Given a string, find the length of the smallest window that contains every 
distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final
five letters.
"""




def find_smallest_window(s: str) -> int:
    # Get all distinct characters
    distinct_chars = set(s)
    n = len(s)
    min_window = n
    
    # Try all possible windows
    for start in range(n):
        # Keep track of found characters
        found_chars = set()
        
        # Expand window until we find all distinct characters
        for end in range(start, n):
            found_chars.add(s[end])
            
            # If we found all distinct characters, update min_window
            if len(found_chars) == len(distinct_chars):
                min_window = min(min_window, end - start + 1)
                break
                
    return min_window


def find_smallest_window_efficient(s: str) -> int:
    # Get all distinct characters
    distinct_chars = set(s)
    n = len(s)
    
    # If string is empty or has only one character
    if n == 0 or len(distinct_chars) == 1:
        return 1
    
    # Initialize frequency counter
    char_freq = {}
    start = 0
    min_window = n
    unique_chars_found = 0
    
    # Process each character
    for end in range(n):
        # Add current character to frequency counter
        char_freq[s[end]] = char_freq.get(s[end], 0) + 1
        
        # If this is the first occurrence of the character
        if char_freq[s[end]] == 1:
            unique_chars_found += 1
        
        # If we found all unique characters
        while unique_chars_found == len(distinct_chars):
            # Update min_window if current window is smaller
            min_window = min(min_window, end - start + 1)
            
            # Remove characters from the start of window
            char_freq[s[start]] -= 1
            if char_freq[s[start]] == 0:
                unique_chars_found -= 1
            start += 1
    
    return min_window

# Test cases
def test_smallest_window():
    # Test case 1: Given example
    assert find_smallest_window("jiujitsu") == 5, "Test case 1 failed"
    
    # Test case 2: All characters are same
    assert find_smallest_window("aaaa") == 1, "Test case 2 failed"
    
    # Test case 3: All characters are different
    assert find_smallest_window("abcd") == 4, "Test case 3 failed"
    
    # Test case 4: Multiple occurrences of characters
    assert find_smallest_window("aabcbcda") == 4, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_smallest_window()
    
    # Additional example
    s = "jiujitsu"
    result = find_smallest_window(s)
    print(f"\nInput string: {s}")
    print(f"Length of smallest window containing all distinct characters: {result}")
    s = "aaaa"
    result = find_smallest_window(s)
    print(f"\nInput string: {s}")
    print(f"Length of smallest window containing all distinct characters: {result}")
    s = "abcd"
    result = find_smallest_window(s)
    print(f"\nInput string: {s}")
    print(f"Length of smallest window containing all distinct characters: {result}")
    s = "aabcbcda"
    result = find_smallest_window(s)
    print(f"\nInput string: {s}")
    print(f"O(N) Length of smallest window containing all distinct characters: {result}")

    s = "jiujitsu"
    result = find_smallest_window_efficient(s)
    print(f"\nInput string: {s}")
    print(f"O(N) Length of smallest window containing all distinct characters: {result}")
    s = "aaaa"
    result = find_smallest_window_efficient(s)
    print(f"\nInput string: {s}")
    print(f"O(N) Length of smallest window containing all distinct characters: {result}")
    s = "abcd"
    result = find_smallest_window_efficient(s)
    print(f"\nInput string: {s}")
    print(f"O(N) Length of smallest window containing all distinct characters: {result}")
    s = "aabcbcda"
    result = find_smallest_window_efficient(s)
    print(f"\nInput string: {s}")
    print(f"O(N) Length of smallest window containing all distinct characters: {result}")