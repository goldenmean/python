'''
Given an integer, find the next permutation of it in absolute order.
 For example, given 48975, the next permutation would be 49578
'''

def next_larger_permutation(number):
    digits = list(map(int, str(number)))
    n = len(digits)
    i = n-2

    while i >= 0 and digits[i] >= digits[i+1]:
        i-= 1

    if i == -1:
        # current permutation is largest, so cannot return any larger permutation
        return -1
    
    j = n-1
    #Find rightmost digit that is greater than the digit at index i
    while digits[j] <= digits[i]:
        j-=1
    #Swap digits at i, j
    digits[i], digits[j] = digits[j], digits[i]
    # We got a larger number after above swap, so Reverse the digits from i+1 to the end so we get a larger permutation
    digits = digits[:i+1] + digits[i+1:][::-1]

    return int(''.join(map(str, digits)))

   

#num = 48975
num = 43217
print(next_larger_permutation(num))