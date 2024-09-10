'''
Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character
of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the
following circle: chair --> racket --> touch --> height --> tunic --> chair
'''

def is_word_circle(words):
    startword = dict()
    endword = dict()

    for w in words:
        start = w[0]
        end = w[-1]

        startword[start] = startword.get(start, 0) + 1
        endword[end] = endword.get(end, 0) + 1
    
    for k, v in startword.items():
        if k not in endword or v != endword[k]:
            return False
    return True                            


words = ['chair', 'height', 'racket', 'touch', 'tuning']
b = is_word_circle(words)
if b:
    print("Arranging the words in a circle is possible")
else:
    print("Arranging the words in a circle is not possible")

