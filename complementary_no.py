def find_complement(num): 

    # Find the number of bits in the binary representation of num 

    num_bits = num.bit_length() 

    print(f"num_bits is {num_bits}")
     
    # Generate a number with all bits set to 1 of the same length as num 
    all_bits_set = (1 << num_bits) - 1      
    print(f"all_bits_set is {all_bits_set}")

    # Return the XOR of num with all_bits_set, which flips all the bits 
    return num ^ all_bits_set 
 

# Test the function with the given example 

number = int(input("Enter the number: "))

print(find_complement(number))