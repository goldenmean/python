
'''
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''
'''
This is a classical problem in computer science known as the Edit Distance problem
and is commonly solved using dynamic programming - Bottom up tabulation approach
Time Complexity: O(m*n)
'''

def minDistance(word1: str, word2: str) -> int: 
    m, n = len(word1), len(word2)
    # Create dp array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1): 
        dp[0][j]= j
    
    # Fill dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # since current characters are same in both strings, number of operations needed for 
                # converting i chars in str1 to j chars in str2, would be same number of operations 
                # that were needed for converting previous substrings : 
                # i-1 chars in str1 to j-1 chars in str2
                dp[i][j] = dp[i-1][j-1]                
            else:
                #If current characters are different in both strings then we have three choices 
                # to convert i chars in str1 to j chars in str2: 1] Delete 2] Insert 3] Replace
                # 1(current operation) + min(Delete, Insert, Replace) 
                '''
                dp[i-1][j]: Insert operation (since we're moving back in word1 but staying at the same point in word2, 
                        it's like adding a character to word1 to match word2[j]).
                dp[i][j-1]: Delete operation (advance in word1 but not in word2, effectively removing a character from word1).
                dp[i-1][j-1]: Replace operation (change word1[i] to match word2[j] and move both strings forward).
                '''
                dp[i][j] = 1 + min(dp[i-1][j], # Insert
                                   dp[i][j-1], # Delete
                                   dp[i-1][j-1]) # Replace
                
    # Return minimum number of operations
    return dp[m][n]

   

#word1 = "horse"; word2 = "ros"
word1 = "intention"; word2 = "execution"

print(minDistance(word1, word2))