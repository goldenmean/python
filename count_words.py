'''
Given a string, text, return how many times you can form the string “programming”.

Ex: Given the following text…

text = "mingabcprojklgram", return 1.
Ex: Given the following text…

text = "rammingabcprogrammingdefprog", return 2.
'''
from collections import Counter

def count_of_words(text, string):
    c_text = Counter(text)
    c_str = Counter(string)
    mintimes = float("+inf")

    for k, v in c_str.items():
        if k not in c_text or c_text[k] < v:
            return 0
        else:
            mintimes = min(mintimes, c_text[k]//v )

    return mintimes

str = "programming"

#inptext = "mingabcprojklgram"
#inptext = "rammingabcprogrammingdefprog"
inptext = "programmingprogrammingprogramming"

print(count_of_words(inptext, str))