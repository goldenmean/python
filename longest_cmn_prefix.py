'''
["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"

'''

def long_cmn_prefix(strs):
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    prefix = ""
    
    for i in range(min_len):
        char = strs[0][i]
        
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    
    return prefix



#test=["colorado", "color", "cold"]
#test=["a", "b", "c"]
test=["spot", "spotty", "spotted"]

print(long_cmn_prefix(test))



'''
Same problem solved using Trie O(N) complexity: 

Yes, it's possible to solve this problem in $$O(N)$$ time complexity, where $$N$$ is the total number of characters across all strings. This can be achieved by using a Trie (prefix tree), a tree-like data structure that stores strings in a way that allows for efficient prefix queries. 

Here's a Python solution using a Trie:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfString = True

    def longestCommonPrefix(self):
        prefix = ""
        node = self.root
        while node and len(node.children) == 1 and not node.endOfString:
            node = next(iter(node.children.values()))
            prefix += next(iter(node.children))
        return prefix

def long_cmn_prefix(strs):
    trie = Trie()
    for word in strs:
        trie.insert(word)
    return trie.longestCommonPrefix()
```

This code first inserts all the strings into the Trie. Then it traverses down the Trie until it finds a node with more than one child (which means the strings start to diverge) or a node that marks the end of a string. The traversed path forms the longest common prefix.

Please note that while the time complexity for the problem is $$O(N)$$ with this approach, the space complexity is higher than the previous solution because of the additional space required to store the Trie. 😊

Source: Conversation with Bing, 21/12/2023
(1) github.com. https://github.com/sm2774us/full_stack_interview_prep_2021/tree/5c21b8641654e6212fd4caef313b95891efeab56/company_wise_prep%2Ffacebook_interview_prep_2021%2FREADME.md.
(2) github.com. https://github.com/Zhenye-Na/leetcode/tree/cf2d431ab22fadd83e66b42d3a39e69d083f149d/python%2F1268.search-suggestions-system.py.

'''