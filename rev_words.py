'''
Given a string s, reverse the words.
Note: You may assume that there are no leading or trailing whitespaces and 
each word within s is only separated by a single whitespace.

Ex: Given the following string s…

s = "The Daily Byte", return "Byte Daily The".
'''


def reverse_words(s):

    lw=s.split(' ')
    print(lw[::-1])
    

    
    
strg="The Daily Byte"
reverse_words(strg)