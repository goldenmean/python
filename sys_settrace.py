# Using settrace API from sys module 

import sys
import time

call_times = {}

def profiler(frame, event, arg):
    if event == 'call':
        call_times[frame.f_code.co_name] = time.time()
    elif event == 'return':
        func_name = frame.f_code.co_name
        if func_name in call_times:
            elapsed = time.time() - call_times[func_name]
            print(f"{func_name} took {elapsed:.6f} seconds")
    return profiler

sys.settrace(profiler)

# Example usage
def slow_function():
    time.sleep(1)

slow_function()



import threading

def print_thread_ident():
    print(f"Thread ID: {threading.current_thread().ident}")

thread = threading.Thread(target=print_thread_ident)
thread.start()
thread.join()