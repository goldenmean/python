'''
This question is asked by Microsoft. Given a string, return the index of its first unique character. 
If a unique character does not exist, return -1.

Ex: Given the following strings...

"abdabc", return 2
"thedailybyte", return 1
"developer", return 0

'''

def unique_char_idx(str):
    charfreq = {}
    for c in str:
        if c in charfreq:
            charfreq[c] += 1
        else:
            charfreq[c] = 1
        
    for v in charfreq.values():
        if v == 1:
            print(v) 
            return v
         





str="abdabc"
unique_char_idx(str)