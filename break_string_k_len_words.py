"""
Given a string s and an integer k, break up the string into multiple lines such that each line
has a length of k or less. You must break it up so that words don't break across lines. Each 
line has to have the maximum possible amount of words. If there's no way to break the text up,
then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly 
one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you 
should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the
 list has a length of more than 10.
"""

def break_str_into_words_k_length(s, k):
    w = s.split(" ")
    words = ''
    soln = []
    cum_total = 0
    #print(len(w))
    for i in range(len(w)):
        #print(w[i])
        if len(w[i]) > k:
            return None
        
        cum_total += len(w[i])
        if cum_total <= k:
            if i == 0:
                words = w[i]
            else:
                words = words + ' ' + w[i]
        else:
            soln.append(words)
            words = w[i]
            cum_total = len(w[i])
        #print(f"words = {words}")   
    if len(words) > 0:
        soln.append(words)
    return  soln

# test example
s = "the quick brown fox jumps over the lazy dog"
k = 10
print(break_str_into_words_k_length(s, k))

            
