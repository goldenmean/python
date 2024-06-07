import asyncio
import websockets

async def hello():
    uri = "ws://localhost:5678"
    async with websockets.connect(uri) as tp:
        name = input("What's your name? ")
        await tp.send(name)
        print(f"> {name}")

        greeting = await tp.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
