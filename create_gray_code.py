



def generate_gray_code(n):
    if n == 0:
        return []
    elif n == 1:
        return ['0', '1']
    else:
        gray_code = generate_gray_code(n - 1)
        gray_code_extended = ['0' + g for g in gray_code] + ['1' + g for g in reversed(gray_code)]
        return gray_code_extended

# Test the function
#print(generate_gray_code(2))
print(generate_gray_code(3))