
import asyncio
import websockets

connected = set()

async def echo(websocket, path):
    print("📡 Client connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            print(f"💬 Received: {message}")
            await asyncio.wait([ws.send(message) for ws in connected])
    finally:
        connected.remove(websocket)

start_server = websockets.serve(echo, "localhost", 5678)

print("🚀 Overlay WebSocket Server started at ws://localhost:5678")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
