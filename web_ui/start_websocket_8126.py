import asyncio
import websockets
import json

connected = set()

async def handler(websocket):
    connected.add(websocket)
    print("[CONNECTED] Client connected.")
    try:
        async for message in websocket:
            print(f"[RECEIVED] {message}")
            for client in connected:
                await client.send(message)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        connected.remove(websocket)
        print("[DISCONNECTED] Client disconnected.")

async def main():
    print("[STARTING] WebSocket server on ws://localhost:8126")
    async with websockets.serve(handler, "localhost", 8126):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())