def permute(s, answer=''):
    if len(s) == 0:
        print(answer, end='\n')
        return
    for i in range(len(s)):        
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        print(f"s is {s}, i is {i}, ch is {ch}, answer is {answer+ch}")
        permute(rest, answer + ch)

# Test the function
s = "abc"
permute(s)  # Output: abc acb bac bca cab cba