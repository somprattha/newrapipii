
import asyncio
import websockets
import json
import random

connected_clients = set()

sample_chats = [
    {"author": "แฟนคลับA", "text": "น่ารักมากเลยยย~"},
    {"author": "แฟนคลับB", "text": "ร้องเพลงอีกหน่อยสิ~"},
    {"author": "แฟนคลับC", "text": "ฮ่าๆ ขำมาก!"},
    {"author": "แฟนคลับD", "text": "วันนี้ดูเศร้าๆ นะ"},
]

emotions = ["Happy", "Sad", "Angry", "Flushed", "Neutral"]
emoji_map = {
    "Happy": "😄", "Sad": "😭", "Angry": "😡", "Flushed": "😳", "Neutral": "😶"
}

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        while True:
            msg = random.choice(sample_chats)
            em = random.choice(emotions)
            await websocket.send(json.dumps({
                "author": msg["author"], "text": msg["text"], "emotion": em
            }))
            await asyncio.sleep(6)
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("✅ WebSocket Chat+Emotion Server started on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
