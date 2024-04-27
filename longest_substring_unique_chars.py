'''
Given a string s, return the length of the longest substring that contains only unique characters.

Ex: Given the following string s…

s = "ababbc", return 2.
Ex: Given the following string s…

s = "abcdssa", return 5
'''


def non_repeating_substring(s):
    n=len(s)
    seen=set()
    maxlen=0
    l=0

    for r in range(n):
        print(f"char is {s[r]}")
        while s[r] in seen:
            print(f"repeated char : set is {seen}")
            seen.remove(s[l])
            l+=1

        print(seen)
        seen.add(s[r])
        maxlen=max(maxlen,r-l+1)
        print(seen)
   
    return maxlen


#strng="ababbc"
#strng="abcdssa"
#strng="ababcb"
#strng="ajit"
#strng="aaaa"
#strng="baa"
strng="aba"
print(non_repeating_substring(strng))


