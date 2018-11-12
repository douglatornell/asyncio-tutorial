import asyncio
import websockets


async def beat1(websocket):
    while True:
        await asyncio.sleep(1)
        await websocket.send("💚")


async def beat2(websocket):
    while True:
        await asyncio.sleep(2)
        await websocket.send("💓")


async def active_ws_handler(websocket):
    await asyncio.gather(beat1(websocket), beat2(websocket))


async def reactive_ws_handler(websocket):
    async for message in websocket:
        if message.lower() == "ping":
            await websocket.send("pong")


async def ws_handler(websocket, path):
    await asyncio.gather(active_ws_handler(websocket), reactive_ws_handler(websocket))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(ws_handler, "0.0.0.0", 9999)
    )
    asyncio.get_event_loop().run_forever()
