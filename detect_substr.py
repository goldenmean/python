'''
How would you write a function to detect a substring in a string?
If the substring can be found in the string, return the index at which it starts. Otherwise, return -1
Length of both the given strings <=100000
The strings would never be null
The strings will only consist of lowercase letters
Expected time complexity : O(n)
Expected space complexity : O(1)

'''

def det_subs(strg, substrg):
    idx1=0
    idx2=0
    #print(strg)
    while idx1 < len(strg):
        if strg[idx1] == substrg[idx2]:
            if idx2 == len(substrg)-1: 
                print(f"idx1 is {idx1}, idx2 is {idx2}")
                return idx1-idx2
            idx2+=1 
        else:
            idx2=0
        idx1+=1
    
    return -1                   
                
#string = "ajit deshpande"
#substr = "pin"

string="home is where peace is"
substr=" peace"

print(det_subs(string,substr))              