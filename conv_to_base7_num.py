
'''
Given an integer, num, return its base seven representation as a string.
Ex: Given the following num... num = 42, return “60”.
'''



def base_seven(num):
    if num == 0:
        return ''
    else:
        return base_seven(num // 7) + str(num % 7)

num = 42
result = base_seven(num)
print(result)  # Output: 60




