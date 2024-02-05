
'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
 repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA"
 would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and 
consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

def rlencode(s):
    if len(s) == 0:
        return ""
    
    cnt=1
    res=""
    i=1
    while i < len(s):
        if s[i] == s[i-1]:
            cnt+=1
        else:
            res=res+str(cnt)
            res=res+s[i-1]
            cnt=1
        i+=1
    
    res=res+str(cnt)
    res=res+s[i-1]
    return res
    
    
#s="AAAABBBCCDAA"  
s="ajit"  
print(rlencode(s))
    