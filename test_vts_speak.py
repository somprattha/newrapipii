from websockets import connect
import asyncio
from gtts import gTTS
import pygame

# ฟังก์ชันสำหรับพูด
def speak(text):
    tts = gTTS(text=text, lang='th')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass  # รอให้เสียงเล่นจนจบ

# ฟังก์ชันการเชื่อมต่อกับ VTube Studio
async def test_connection():
    uri = "ws://127.0.0.1:8001"  # เชื่อมต่อกับ WebSocket ของ VTube Studio
    try:
        async with connect(uri) as websocket:
            print("เชื่อมต่อกับ WebSocket ของ VTube Studio สำเร็จ!")

            # ส่งคำสั่งให้ VTube Studio เปลี่ยนอารมณ์
            await websocket.send('{"jsonrpc": "2.0", "method": "SetExpression", "params": {"expression": "happy"}}')
            print("ส่งคำสั่งไปยัง VTube Studio เพื่อเปลี่ยนอารมณ์")

            # ทดสอบการพูด
            speak("สวัสดีครับ")
            print("AI กำลังพูด")

    except Exception as e:
        print(f"ไม่สามารถเชื่อมต่อ: {e}")

# เรียกใช้งาน
asyncio.run(test_connection())
