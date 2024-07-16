


# Example of Daemon thread which will exit gracefully when main thread exits
# Python doesnt really supprt detachable threads like C(Posix),C++(std::thread)

import threading
import time

def next_fun():
    for i in range(5):
        print("Hello in between the other thread that is running")

def worker():
    print("Worker Thread starting\n")
    time.sleep(5)  # Simulate some work
    print("Worker Thread finishing")

# Create a daemon thread
t = threading.Thread(target=worker)
t.daemon = True
t.start()
next_fun()
t.join()
print("Main thread exiting")

