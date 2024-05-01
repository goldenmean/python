'''
Given a string of words delimited by spaces, reverse the words in string.
 For example, given "hello world here", return "here world hello"
'''

def rev_words_in_sentence(s):
    words=s.split()
    reversed_words = ' '.join(words[::-1])

