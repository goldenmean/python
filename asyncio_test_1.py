'''
Coroutines use the await keyword to yield control back to the event loop, which 
then manages the execution of other tasks. This mechanism is crucial for handling
I/O-bound and high-latency operations asynchronously, improving the performance
and responsiveness of applications.

In this example, greet is a coroutine that takes a name and a delay as arguments.
It uses await asyncio.sleep(delay) to pause its execution for the specified delay,
allowing other tasks to run in the meantime. 
The main coroutine gathers several instances of the greet coroutine and schedules
them to run concurrently using asyncio.gather. 
Finally, asyncio.run(main()) starts the event loop and executes the main coroutine.
Coroutines, along with the event loop and tasks, form the core components of asyncio,
enabling efficient asynchronous programming in Python.

'''


import asyncio

async def greet(name, delay):
    print(f"Entered greet with {name} and {delay}")
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    await asyncio.gather(
        greet("Charlie", 3),
        greet("Alice", 2),
        greet("Bob", 1),
        
    )

if __name__ == "__main__":
    asyncio.run(main())

    