
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

'''

# Function currying in Python using closures
def curried_multiply(a):
    def next(b):
        def final(c):
            print(f"a={a}, b={b}, c={c}")
            return a * b * c
        return final
    return next

result = curried_multiply(2)(3)(4)
print(result)  # Output: 24

# Function currying involving Closures where the closure next and final also capture
# the values of enclosing local variables and the enclosing function parameters
def other_curried_multiply(a):
    random1 = 10
    def next(b): 
        random2 = 20
        def final(c):
            print(f"a={a}, b={b}, c={c}, radom1={random1}, random2={random2}")
            return a * b * c * random1 * random2
        return final
    return next

result = other_curried_multiply(2)(3)(4)
print(result)  