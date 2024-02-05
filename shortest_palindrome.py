'''
What's the shortest palindrome that can be returned? For example, the following above string should return:

JS
shortestPalindrome("bubble")
// "elbbubble"
Constraints
Length of the given string <= 1000
The string can contain any ASCII letters
Expected time complexity : O(n)
Expected space complexity : O(1)

'''

def shortest_palindrome(s):
    pf=""
    l=0
    r=len(s)-1
    while l < r:
        if s[l] != s[r]:
            pf=pf+s[r]
            r-=1
        else:
            r-=1
            l+=1
    
    return pf+s
	


#s="bubble"
#s="ajit"
#s="manasi"
s="isha"
print(shortest_palindrome(s))