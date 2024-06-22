'''
Given a list of words, find all pairs of unique indices such that the concatenation of the
 two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
'''

def indices_palindromes(words):
    pairs = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            #print(words[i], words[j])
            tmpword = words[i] + words[j]
            if tmpword == tmpword[::-1]:
                pairs.append((i, j))
            tmpword = words[j] + words[i]
            if tmpword == tmpword[::-1]:
                pairs.append((j, i))
    return pairs



print(indices_palindromes(["code", "edoc", "da", "d"]))