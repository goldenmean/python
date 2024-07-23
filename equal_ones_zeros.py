'''
Given a binary string s, return the number of contiguous substrings that 
contains the same number of zeroes and ones.
Note: Each substring’s zeroes and ones must be grouped together.

Ex: Given the following string s…

s = "101", return 2 ("10" and "01").
Ex: Given the following string s…

s = "1011101", return 4 ("10", "01", "10", "01")
'''

def count_equal_zeroes_ones_substrings(s):
    # Initialize variables to keep track of the current and previous character counts
    prev_run_length = 0
    curr_run_length = 1
    count = 0
    
    for i in range(1, len(s)):
        print(f"bit is {s[i]} and previous bit is {s[i-1]}")
        if s[i] == s[i-1]:
            # If the current character is the same as the previous one, increment the current run length
            curr_run_length += 1
        else:
            # If the current character is different, it means a transition has occurred
            # The count of substrings is incremented by the minimum of the current and previous run lengths
            count += min(prev_run_length, curr_run_length)
            print(f"prev_run_length is {prev_run_length} curr_run_length is {curr_run_length} count is {count}")
            # The previous run length is updated to the current run length
            prev_run_length = curr_run_length
            # The current run length is reset to 1
            curr_run_length = 1
    
    # After the loop, we do one final addition to the count
    # to account for the last run
    count += min(prev_run_length, curr_run_length)
    
    return count

# Test cases
#print(f"Ans is", count_equal_zeroes_ones_substrings("1010")) 
#print(f"Ans is", count_equal_zeroes_ones_substrings("1100")) 
#print(f"Ans is", count_equal_zeroes_ones_substrings("111010")) 
#print(count_equal_zeroes_ones_substrings("101")) # Output: 2
#print(count_equal_zeroes_ones_substrings("1011101")) # Output: 4
#print(f"Ans is", count_equal_zeroes_ones_substrings("11011")) 
print(f"Ans is", count_equal_zeroes_ones_substrings("111001100")) 