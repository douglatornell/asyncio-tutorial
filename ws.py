import asyncio
import websockets


async def ws_handler(websocket, path):
    while True:
        await asyncio.sleep(1)
        await websocket.send("💚")


# initialize websocket server from this handler

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(ws_handler, "0.0.0.0", 9999)
    )
    asyncio.get_event_loop().run_forever()
