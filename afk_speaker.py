import time
from multi_tts_engine import speak
import random

afk_lines = [
    "เจ้าของช่องพักสายตาแป๊บนึงนะคะ~",
    "ตอนนี้ราปิปี้ขอเป็นคนคุยกับทุกคนก่อนน้า~ 💕",
    "อย่าเพิ่งไปไหนนะ รอเจ้าของช่องกลับมาก่อน~"
]

def start_afk_mode(duration_min=5):
    print(f"[AFK Mode] พูดแทนเจ้าของ {duration_min} นาที")
    end_time = time.time() + duration_min * 60
    while time.time() < end_time:
        speak(random.choice(afk_lines))
        time.sleep(45)