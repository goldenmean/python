

'''
Given a string and a pattern, find the starting indices of all occurrences of the
pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7]
'''


#Return all indices where substring needle is found in the given string haystack
def find_all_occurrences(haystack, needle): 
    h=len(haystack)
    n = len(needle) 
    res=[]
    for i in range(h):
        j=0 
        for k in range(i,h): 
            #print(i,j,k)
            if haystack[k]==needle[j]: 
                j+=1 
            else: 
                break

            if j == n: 
                #return i # return is if you want to return the index of 1st occurrence
                res.append(i)
                break
                #print(i,j,k)
    return res  

# Example 
print(find_all_occurrences("hello", "ll"))
print(find_all_occurrences("abracadabra", "abr"))
       