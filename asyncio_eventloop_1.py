

import asyncio


def next_fun():
    for i in range(5):
        print("Hello")

# Define an asynchronous function
async def main():
    # Now you can use await here
    result = await asyncio.sleep(3)
    next_fun()
    print(result)

# Get the current event loop
loop = asyncio.new_event_loop()

try:
    # Run the main coroutine until it completes
    loop.run_until_complete(main())    
finally:
    # Close the loop when done
    loop.close()


'''
# Define an asynchronous function
async def main():
    # Now you can use await here
    result = await asyncio.sleep(10)
    print(result)

# Since we cannot use await at the top level, we call our async function like this
asyncio.run(main())

'''