# web_socket_overlay.py — ส่งข้อความไปยัง HTML Overlay
import asyncio
import websockets
import json
import threading

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for _ in websocket:
            pass
    finally:
        clients.remove(websocket)

def start_websocket_server():
    asyncio.set_event_loop(asyncio.new_event_loop())
    start_server = websockets.serve(handler, "localhost", 7869)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

def send_vip_overlay(username, message, vip_level="⭐"):
    emoji = {"⭐":"✨", "🌟":"🌟", "💖":"💖", "👑":"👑"}.get(vip_level, "⭐")
    data = json.dumps({"username": username, "message": message, "emoji": emoji})
    for client in clients.copy():
        asyncio.run_coroutine_threadsafe(client.send(data), asyncio.get_event_loop())

# เริ่ม WebSocket server แบบเบื้องหลัง
def launch():
    t = threading.Thread(target=start_websocket_server, daemon=True)
    t.start()