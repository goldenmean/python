
import inspect

def current_function_name():
    #Current function name
    print(f"Current function is {inspect.currentframe().f_code.co_name}")
    #Current line number in the file
    print(f"Line number is {inspect.currentframe().f_lineno}")
    # Filename
    print(f"File name is {inspect.currentframe().f_code.co_filename}")
    # Name of the caller function
    print(f"Caller is {inspect.currentframe().f_back.f_code.co_name}")


def example_function():
    print(f"Current function is {inspect.currentframe().f_code.co_name}")
    #Current line number in the file
    print(f"Line number is {inspect.currentframe().f_lineno}")
    # Name of the caller function
    print(f"Caller is {inspect.currentframe().f_back.f_code.co_name}")
    current_function_name()


#print(inspect.currentframe().f_code.co_name)
#print(inspect.currentframe().f_lineno)

example_function()


