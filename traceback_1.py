

import traceback

def some_function():
    # Some code that might raise an exception
    raise ValueError("This is a sample error")

def main():
    try:
        some_function()
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        print("Full traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    main()


import traceback

def custom_assert(condition, message="Assertion failed"):
    if not condition:
        print(message)
        print("Full traceback:")
        traceback.print_stack()
        raise AssertionError(message)

def some_function():
    # Some code that might fail an assertion
    x = 5
    custom_assert(x == 10, "x should be 10")

def main():
    try:
        some_function()
    except AssertionError as e:
        print(f"Assertion error: {str(e)}")

if __name__ == "__main__":
    main()
    
        