
'''
Given an string, num that represents the string form of an integer, 
return whether or not the number looks the same when turned upside-down.

Ex: Given the following num...

num = “0”, return true.
Ex: Given the following num...

num = “96”, return true.
Ex: Given the following num...

num = “003821”, return false.
'''

def is_same_upside_down(num):
    # Mapping of digits to their upside-down counterparts
    upside_down_mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    
    # Convert the number to its upside-down form
    upside_down_num = []
    
    for digit in num:
        if digit in upside_down_mapping:
            upside_down_num.append(upside_down_mapping[digit])
        else:
            # If the digit does not have an upside-down counterpart, return False
            return False
    
    # Check if the original number is the same as its upside-down version
    print(f"{''.join(upside_down_num[::-1])}")
    return num == ''.join(upside_down_num[::-1])

# Example usage
print(is_same_upside_down("0"))  # Output: True
print(is_same_upside_down("96"))  # Output: True
print(is_same_upside_down("91"))  # Output: True
print(is_same_upside_down("003821"))  # Output: False