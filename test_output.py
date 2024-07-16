
'''
A Python closure is a nested function that retains access to variables from its 
enclosing scope, even after the outer function has finished executing. This mechanism
allows the inner function to "remember" and use the values of variables from the outer
function, effectively creating a "closed-over" scope. Closures are particularly useful
for implementing data privacy, callbacks, and lazy evaluation among other functional
programming concepts. 
'''

#original code without closure
'''
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

'''

'''
#code with closure
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i=i):
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

    
## Example of Python closure
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
print(double(7))  # Output: 14


## Example of Python Generator
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for number in counter:
    print(number)

'''

## Example of Python Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

#Common way to use decorator
#@my_decorator
def say_hello():
    v = 100
    print(f"Hello! v is {v}")

#say_hello()

#Another way to use decorator
newfunc = my_decorator(say_hello)
newfunc()