
import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket, path):
    print(f"[CONNECTED] {websocket.remote_address}")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"[RECEIVED] {message}")
            # ถ้าต้องการ broadcast ไปยังทุก client
            await asyncio.gather(*[client.send(message) for client in connected_clients if client != websocket])
    except websockets.exceptions.ConnectionClosed:
        print(f"[DISCONNECTED] {websocket.remote_address}")
    finally:
        connected_clients.remove(websocket)

async def main():
    print("[STARTING] WebSocket server on ws://localhost:8124/ws")
    async with websockets.serve(handler, "localhost", 8124):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[STOPPED] WebSocket server terminated.")
