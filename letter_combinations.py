"""
Give python code to solve this coding problem : 
Write a function that takes a string containing digits from 2 to 9 and returns all possible letter combinations that the number could represent. The mapping of digits to letters follows the old phone keypad representation.
Input:
digits: A string containing digits between 2 and 9 (e.g., "23").

Output:
A list of strings, where each string represents a possible letter combination formed from the given digits.

Mapping:
The mapping of digits to letters is as follows:

2: ["a", "b", "c"]
3: ["d", "e", "f"]
4: ["g", "h", "i"]
5: ["j", "k", "l"]
6: ["m", "n", "o"]
7: ["p", "q", "r", "s"]
8: ["t", "u", "v"]
9: ["w", "x", "y", "z"]

"""

def letterCombinations(digits):
     # Return empty list if input is empty
    if not digits:
        return []
    
    # Define the phone keypad mapping
    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    def backtrack(combination, next_digits):
        # If no more digits to process, add the combination
        if not next_digits:
            result.append(combination)
            return
            
        # Get the current digit and its corresponding letters
        current_digit = next_digits[0]
        letters = digit_map[current_digit]
        
        # Recursively build combinations
        for letter in letters:
            backtrack(combination + letter, next_digits[1:])
            
    result = [ ]
    backtrack("", digits)
    return result


# Example usage
print("Test case 1", letterCombinations("23"))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print("Test case 2",letterCombinations("234"))


#Another backtracking solution 

"""
def letter_combinations(digits):
    if not digits:
        return []

    # Mapping of digits to letters
    digit_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def backtrack(index, path):
        # If the path is complete, add it to the results
        if len(path) == len(digits):
            combinations.append(''.join(path))
            return

        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        letters = digit_map[current_digit]

        # Try all letters for the current digit
        for letter in letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

# Test the function
print(letter_combinations("23"))
This solution uses a backtracking approach to generate all possible combinations. Here's how it works:

We define a mapping of digits to their corresponding letters.
We use a recursive backtrack function to generate combinations.
In each recursive call, we try all letters for the current digit and move to the next digit.
When we've processed all digits (i.e., the path length equals the number of digits), we add the current combination to our results.
We use backtracking by removing the last added letter before trying the next one.
The time complexity is O(4^N * N), where N is the number of digits. This is because in the worst case (when the digits are 7 or 9), we have 4 choices for each digit, and we're creating strings of length N.

"""