'''
 Given a dictionary of words and a string made up of those words (no spaces), return the
   original sentence in a list. If there is more than one possible reconstruction, 
   return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
 you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

def reconstruct_sentence(words, string):
    word_set = set(words)
    memo = {}

    def backtrack(s):
        if s in memo:
            return memo[s]
        #Full string processed - we reached the end of string
        if not s:
            return []
        for word in word_set:
            if s.startswith(word):
                result = backtrack(s[len(word):])
                if result is not None:
                    memo[s] = [word] + result
                    return memo[s]
        memo[s] = None
        return None

    return backtrack(string)

# Example usage
words1 = ['quick', 'brown', 'the', 'fox']
string1 = 'thequickbrownfox'
print(reconstruct_sentence(words1, string1))  # Output: ['the', 'quick', 'brown', 'fox']

words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string2 = 'bedbathandbeyond'
print(reconstruct_sentence(words2, string2))  # Output: ['bed', 'bath', 'and', 'beyond'] or ['bedbath', 'and', 'beyond']