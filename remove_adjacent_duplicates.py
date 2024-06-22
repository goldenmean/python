


def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()  # Found duplicate, remove the top element
        else:
            stack.append(char)
    return ''.join(stack)

# Example usage
#input_string = "abbaca" #returns ca
#input_string = "abba" #returns empty string output
input_string = "abbaa" #returns a
input_string="ajit"
output_string = remove_adjacent_duplicates(input_string)
print(output_string)

