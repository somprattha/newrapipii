# youtube_event_handler.py

from core.managers.expression_manager import ExpressionManager
from core.managers.tts_manager import TTSManager
import random
import asyncio

async def on_new_subscribe(username: str):
    # รายชื่อข้อความที่สามารถสุ่มใช้ได้
    messages = [
        f"ขอบคุณสำหรับการติดตามนะคะคุณ {username}~!",
        f"ยินดีต้อนรับเข้าสู่ครอบครัวราปิปี้ค่า~ ขอบคุณที่ติดตามนะคะ {username}!",
        f"อ๊าา~ ขอบคุณสำหรับการติดตามนะ คุณ {username}!",
        f"{username} ติดตามแล้วว~ ดีใจที่สุดเลย~!"
    ]

    # รายชื่ออารมณ์ (expression) ที่เหมาะกับโหมดดีใจ
    expressions = ["joy", "excited", "happy", "sparkle"]

    # สุ่มข้อความและอารมณ์
    message = random.choice(messages)
    expression = random.choice(expressions)

    try:
        # ตั้งอารมณ์
        await ExpressionManager().safe_set_expression(expression)
        await asyncio.sleep(0.3)  # หน่วงนิดเพื่อ sync อารมณ์

        # พูดข้อความ
        await TTSManager().speak(message)

    except Exception as e:
        print(f"[Subscribe Event Error] {e}")
        # fallback: พูดแบบเรียบง่าย
        await TTSManager().speak(f"ขอบคุณที่ติดตามนะคะคุณ {username}")
