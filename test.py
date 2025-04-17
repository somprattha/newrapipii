import websockets
import asyncio

async def test_connection():
    try:
        async with websockets.connect("ws://localhost:8001") as ws:
            print("✅ เชื่อมต่อสำเร็จ")
    except Exception as e:
        print(f"❌ การเชื่อมต่อล้มเหลว: {str(e)}")

asyncio.run(test_connection())