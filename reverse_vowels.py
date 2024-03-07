'''
This question is asked by Facebook. Given a string, reverse the vowels of it.
Note: In this problem y is not considered a vowel.

Ex: Given the following strings s…

s = "computer", return "cemputor"
Ex: Given the following strings s…

s = "The Daily Byte", return "The Dialy Byte"
'''

def rev_vowels(s):
    vowels = ("a","e","i","o","u","A","E","I","O","U")
    N=len(s)
    lvidx=[]
    #vidx=set() #set of vowel indices
    #Get the string as a list of chars to modify the vowel locations 
    b=list(s)
    
    #First find all vowels and their indices 
    for i in range(N):
        if s[i] in vowels:
            print(s[i])     
            lvidx.append(i)
    
    print(f"vowel indices are {lvidx}")
    
    #Swap the characters at those indices
    l=0
    r=len(lvidx)-1
    p1=0
    while p1 < N//2 and l<r:
        if p1 in lvidx:
            b[lvidx[r]],b[lvidx[l]] = b[lvidx[l]],b[lvidx[r]]
            l+=1 
            r-=1            
            #print(f"inside while",b[lvidx[l]],b[lvidx[r]])        
        p1+=1

    #print(f"after reversing b is {b}")

    #covert the modified list b with vowels reversed, back to string
    res=''.join(b)
    #print(f"after converting list to string res is {res}")
    return res
    
#strg = "computer"
#strg = "The Daily Byte"
strg = "AJIT"
print(strg)
print(rev_vowels(strg))
            