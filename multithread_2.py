

import threading
import time

'''
def run():
    time.sleep(3)
    print("Thread finished.")

# Create a daemon thread
daemon_thread = threading.Thread(target=run)
#daemon_thread.daemon = True
daemon_thread.start()

print("Main thread finished.")

# Thread identifier 
import threading

def print_thread_ident():
    print(f"Thread ID: {threading.current_thread().ident}")

thread = threading.Thread(target=print_thread_ident)
thread.start()
thread.join()

'''

def worker():
    print(f"Worker thread ID: {threading.current_thread().ident} starting")
    time.sleep(5)
    print("Worker done.")

# Create a non-daemon thread
non_daemon_thread = threading.Thread(target=worker)
non_daemon_thread.daemon = False  # This is the default value
non_daemon_thread.start()

print("Main thread waiting for non-daemon thread to finish.")
non_daemon_thread.join()
print("Main thread done after non-daemon thread finished.")