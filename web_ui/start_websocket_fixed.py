import asyncio
import websockets
import json

async def handler(websocket, path):
    print("[CONNECTED] Client connected.")
    try:
        async for message in websocket:
            data = json.loads(message)
            print("📥", data)
    except websockets.exceptions.ConnectionClosed:
        print("[DISCONNECTED] Client disconnected.")

async def main():
    print("[STARTING] WebSocket server on ws://localhost:8126")
    async with websockets.serve(handler, "localhost", 8126):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())