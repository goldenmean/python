'''
You are given a 2D array of characters, and a target string. Return whether or not the
target word exists in the matrix. Unlike a standard word search, the word must be eithe
going left-to-right, or top-to-bottom in the matrix.

'''

'''
Leetcode 79 Wordsearch in all directions - up, down, left, right 
https://www.youtube.com/watch?v=pfiQ_PS1g8E

'''
# Word search - only from left to right and top to bottom
def wordsearch_lr_tb(board, word):
    path = set()
    rows = len(board)
    cols = len(board[0])

    def dfs(r,c,pos):
        if pos == len(word):
            return True

        if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or 
            board[r][c] != word[pos] or (r,c) in path):
            return False
        
        path.add((r,c))
        res = dfs(r+1,c,pos+1) or dfs(r,c+1,pos+1)
        path.remove((r,c))
        return res


    for r in range(rows):
        for c in range(cols):
            if dfs(r,c,0):
                return True
    
    return False


# Test program 
board = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']
  ]
word = "FOAM"

print(wordsearch_lr_tb(board, word))


