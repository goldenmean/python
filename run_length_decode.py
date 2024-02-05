'''
encoded string 10A3B2C1D2A
expected output AAAAAAAAAABBBCCDAA
'''

def run_length_decode(input_string):
    count = ''
    result = ''
    for char in input_string:
        # If the character is numeric . . .
        if char.isdigit():
            # . . . append it to our count
            count += char
        else:
            # Otherwise, we've seen a non-digit character and need to expand it for
            # the decoding process.
            result += char * int(count)
            # Reset count
            count = ''
    return result
    
s="10A3B2C1D2A"
print(run_length_decode(s))