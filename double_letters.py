def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])]) #Case sensitive compare
	#return any([a == b for a, b in zip(string.lower(), string[1:].lower())]) # case insenstive compare
	
print(double_letters("Nono"))
print(double_letters("hello"))
print(double_letters("Eerie"))