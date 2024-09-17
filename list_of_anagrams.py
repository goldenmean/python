from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

# Test cases
words = ['abc', 'bcd', 'cba', 'cbd', 'efg']
print(group_anagrams(words))  # Should print [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

words2 = ['listen', 'silent', 'enlist', 'google', 'gogole']
print(group_anagrams(words2))  # Should print [['listen', 'silent', 'enlist'], ['google', 'gogole']]

words3 = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
print(group_anagrams(words3))

