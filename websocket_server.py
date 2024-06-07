import asyncio
import websockets

async def handle_connection(ws, path):
    print(f"websocket is {ws}, path is {path} ")
    name = await ws.recv()
    greeting = f"Hello, {name}!"
    await ws.send(greeting)
    print(f"< {greeting}")

#Define a asynchronous function async def start_server( ) 
async def start_server():
    print(f"Beginning of start_server( )")
    #websockets.serve creates an asynchronous context manager to cleanup resources properly when the server is stopped.
    #handle_connection is the function that will be called when a new client connects
    async with websockets.serve(handle_connection, "localhost", 5678):
        print("Serving on localhost:5678")
        #await pauses the execution of asynchronous function, but the default event loop runs forever
        await asyncio.Future()  # Run forever
        print("After the asyncio Future")

#start the asynchronous function: start_server( )
#run function executes the coroutine and creates asyncio event loop
asyncio.run(start_server())

