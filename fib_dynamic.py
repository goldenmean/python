


def fib(n):
    new, old = 1, 0
    for i in xrange(n):
        print(new)
        print(old)
        print("before")
        new, old = old, new + old
        print(new)
        print(old)
        print("after")

    return old
	
print fib(6);