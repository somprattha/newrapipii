
import asyncio
import websockets
import json

clients = set()

async def handler(websocket):  # removed 'path'
    print("🟢 Overlay client connected")
    clients.add(websocket)
    try:
        async for message in websocket:
            pass  # server doesn't expect to receive, only send
    finally:
        clients.remove(websocket)
        print("🔴 Overlay client disconnected")

async def broadcast_overlay(text, emotion):
    if clients:
        message = json.dumps({"text": text, "emotion": emotion})
        await asyncio.wait([client.send(message) for client in clients])

async def start_server():
    print("🌐 Starting Overlay WebSocket Server on ws://localhost:8126")
    async with websockets.serve(handler, "localhost", 8126):  # removed path
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(start_server())
