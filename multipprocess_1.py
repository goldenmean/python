

from multiprocessing import Process
import time

def worker():
    print("Worker starting")
    # Simulate some work
    time.sleep(4)
    print("Worker finishing")

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    print("Main process exiting")
    #p.join()  # Optional: Wait for the worker process to finish