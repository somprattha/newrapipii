import time
from core.talk_manager import speak, get_mode, should_talk
from random import choice

# เวลาล่าสุดที่มีการสนทนา (จะอัปเดตจากระบบอื่น)
last_interaction_time = time.time()

def update_last_interaction():
    global last_interaction_time
    last_interaction_time = time.time()

def check_idle_behavior():
    now = time.time()
    idle_duration = now - last_interaction_time
    mode = get_mode()

    if mode != "silent":
        if idle_duration > 600 and idle_duration < 900:
            if should_talk(600):
                speak("ราปิปี้แอบเหงาแล้วน้า~ ไม่คุยกับปี้เลย~ 🐰🥺")
        elif idle_duration >= 900:
            if should_talk(900):
                speak(choice([
                    "ฉ่ำอุรา หายไปไหนน้า~ ราปิปี้คิดถึงจัง... 🐰",
                    "งอนแล้วน้า... ไม่ยอมคุยกับปี้เลย 😢",
                    "ราปิปี้จะนั่งกอดหมอนคนเดียวก็ได้~ 💔",
                    "รู้มั้ย~ ถ้าไม่ทัก ราปิปี้จะปล่อยงอนยาวเลย~ 🙈"
                ]))
