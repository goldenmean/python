
'''
 Given a string, split it into as few strings as possible such that each string is a palindrome.
 For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
 Given the input string abc, return ["a", "b", "c"]
'''
def split_into_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    def dfs(s, i, result):
        if i == len(s):
            return [result]

        res = []
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1]):
                res.extend(dfs(s, j + 1, result + [s[i:j + 1]]))
        return res

    res = dfs(s, 0, [])
    print(len(res))
    return min(res, key=len) if res else []

# Test the function
print(split_into_palindromes("racecarannakayak"))  # ["racecar", "anna", "kayak"]
print(split_into_palindromes("abc"))  # ["a", "b", "c"]

