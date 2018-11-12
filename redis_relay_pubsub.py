import asyncio
import websockets

import aioredis
from aioredis.pubsub import Receiver


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


async def redis_relay(websocket):
    conn = await aioredis.create_connection(("localhost", 6379))
    receiver = Receiver()
    conn.execute_pubsub("subscribe", receiver.channel("marketupdates"))
    while await receiver.wait_message():
        *_, message = await receiver.get()
        await websocket.send(message.decode())


async def ws_handler(websocket, path):
    await asyncio.gather(
        active_ws_handler(websocket),
        reactive_ws_handler(websocket),
        redis_relay(websocket),
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(ws_handler, "0.0.0.0", 9999)
    )
    asyncio.get_event_loop().run_forever()
