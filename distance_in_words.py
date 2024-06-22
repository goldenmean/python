'''
Find an efficient algorithm to find the smallest distance (measured in number of words)
 between any two given words in a string.

For example, given words 
"hello", and "world" and a text content of 
"dog cat hello cat dog dog hello cat world", return 1 because there's only one word
"cat" in between the two words.

'''


def dist_in_words(words,w1,w2):
    indices1 = [i for i, x in enumerate(words) if x == w1]
    indices2 = [i for i, x in enumerate(words) if x == w2]
    
    if len(indices1)==0 or len(indices2)==0:
        return -1   
    
    mindiff = float("+inf")
    
    for i1 in indices1:
        for i2 in indices2:
            diff = abs(i1-i2)-1
            mindiff = min(mindiff, diff)
    
    return mindiff
            
words = ["ajit","hello","my","world","ajit","boy","deshpande"]			
word1 = "ajit" ; word2 = "deshpande"
print(dist_in_words(words,word1,word2))			
