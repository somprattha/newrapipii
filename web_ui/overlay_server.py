import asyncio
import websockets
import json

connected = set()

async def handler(websocket):
    print("📡 Client connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            print("📥", message)
            data = json.loads(message)
            if data.get("type") == "overlay":
                for conn in connected:
                    if conn != websocket:
                        await conn.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected")
    finally:
        connected.remove(websocket)

async def main():
    print("🚀 Overlay WebSocket Server started at ws://localhost:5678")
    async with websockets.serve(handler, "localhost", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())