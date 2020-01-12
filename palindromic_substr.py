#Input is a string 
def num_of_palindromic_substrings(ipstr):
    slen = len(ipstr)
    cnt = 0
    for x in range(slen):
        for y in range((x+1),slen):
            substr = ipstr[x:(y+1)]
            rstr = ''.join(reversed(substr))
            if(substr == rstr):
                cnt += 1
                print "Palindrome sub string number",cnt,":",substr
                
            
    return cnt

#Application test code
    
#Test cases 

t1 = "abaabab"
t2 = "baababa" 
t3 = "abbacada"
t4 = "aza"
t5 = "abba"
t6 = "abacaba"
t7 = "zaza"
t8 = "abcd"
t9 = "abacada"
t10 = 'ab3492a'
t11 = "level"
    
ret =  num_of_palindromic_substrings(t11)
print "Total number of palindromic sub strings is:", ret 
