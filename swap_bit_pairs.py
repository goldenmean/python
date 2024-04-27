'''
Given an unsigned 8-bit integer, swap its even and odd bits. 
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
e.g. 
N=5  bin = 101 => swap pairs of bits =>  1010
For example, 10101010 should be 01010101. 11100010 should be 11010001.
'''

def swap_bit_pairs(N):
    #snum=bin(N)[2:]
    i=0
    bitlist=[]

    while i < 8:
        bit1 = N & 0x1
        bit2 = (N & 0x20) >> 1
        bitlist.append(bit2)    
        bitlist.append(bit1)
        N=N>>2
        i+=2
    
    print(bitlist)
    #construct the new number from its bits in bitlist
    num = 0
    for i, bit in enumerate(bitlist):
        num += bit << i

    print(num)    
    return num

### Another solution giveb by Bing copilot
'''
    # Get all even bits of n
    even_bits = n & 0b10101010

    # Get all odd bits of n
    odd_bits = n & 0b01010101

    # Right shift all even bits
    even_bits >>= 1

    # Left shift all odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    return even_bits | odd_bits

'''

N=5
print(bin(N))
res=swap_bit_pairs(N)
print(bin(res))


