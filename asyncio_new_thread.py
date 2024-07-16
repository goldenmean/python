'''
Asyncio code on a separate thread
https://stackoverflow.com/questions/74145286/python-run-non-blocking-async-function-from-sync-function

'''


import asyncio
import threading

from datetime import datetime
now = datetime.now

def next_fun():
    for i in range(5):
        print("Hello in between the async task which is running in another thread")

async def test_timer_function():
    print(f"\nasync task started at {now()}\n")
    await asyncio.sleep(4)
    print(f"\nasync task ended at {now()}")
    return

def run_async_loop_in_thread():
    asyncio.run(test_timer_function())

def main():
    print(f"Starting timer at {now()}")
    t = threading.Thread(target=run_async_loop_in_thread)
    t.start()
    print(f"Ending timer at {now()}")
    return t

if __name__ == "__main__":
    t = main()
    next_fun()
    t.join()
    print(f"asyncio thread exited normally at {now()}")