import asyncio
import json
import time
from gtts import gTTS
import os
import pygame
from core.vts_controller import VTubeStudioConnector  # เชื่อมต่อกับ VTube Studio

# การตั้งค่าการเชื่อมต่อ VTube Studio
vts = VTubeStudioConnector()

# ไฟล์การตั้งค่า
CONFIG_PATH = "config/persona_config.json"

# ฟังก์ชันโหลดการตั้งค่าจากไฟล์
def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"mode": "talkative", "last_auto_speak_time": 0}  # ค่าเริ่มต้น

# ฟังก์ชันบันทึกการตั้งค่าลงในไฟล์
def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)

# ฟังก์ชันตรวจสอบว่า AI ควรพูดหรือไม่
def should_talk(interval_sec=120):
    cfg = load_config()
    now = time.time()
    if now - cfg["last_auto_speak_time"] >= interval_sec:
        cfg["last_auto_speak_time"] = now
        save_config(cfg)
        return True
    return False

# ฟังก์ชันตั้งค่าโหมดใหม่
def set_mode(new_mode):
    cfg = load_config()
    cfg["mode"] = new_mode
    save_config(cfg)
    print(f"[🧠] เปลี่ยนโหมดพูด: {new_mode}")
    send_emotion_to_vts(new_mode)  # ส่งอารมณ์ไปยัง VTube Studio เมื่อโหมดเปลี่ยน

# ฟังก์ชันดึงโหมดปัจจุบัน
def get_mode():
    return load_config().get("mode", "talkative")

# ฟังก์ชันพูดข้อความด้วย TTS (gTTS)
def speak(text):
    tts = gTTS(text=text, lang='th')
    tts.save("output.mp3")
    os.system("start output.mp3")  # ใช้คำสั่งเล่นเสียง (Windows)

    # หรือใช้ pygame เพื่อเล่นเสียงในพื้นหลัง
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # รอให้เสียงเล่นเสร็จ
        pygame.time.Clock().tick(10)

# ฟังก์ชันส่งอารมณ์ไปยัง VTube Studio
def send_emotion_to_vts(new_mode):
    if new_mode == "talkative":
        vts.set_emotion("happy")  # ส่งอารมณ์ "happy"
    elif new_mode == "playful":
        vts.set_emotion("excited")  # ส่งอารมณ์ "excited"
    elif new_mode == "serious":
        vts.set_emotion("serious")  # ส่งอารมณ์ "serious"
    else:
        vts.set_emotion("neutral")  # ส่งอารมณ์ "neutral"
    print(f"🔮 ส่งอารมณ์: {new_mode} ไปยัง VTube Studio")

# ฟังก์ชันหลัก
async def main():
    if should_talk():  # ตรวจสอบว่า AI ควรพูดหรือไม่
        mode = get_mode()  # ดึงโหมดปัจจุบัน
        if mode == "talkative":
            speak("สวัสดีครับ! วันนี้เป็นวันที่ดีมาก")
        elif mode == "playful":
            speak("ฮ่าๆๆ! มาทำอะไรสนุกๆ กันเถอะ!")
        elif mode == "serious":
            speak("เรามาพูดคุยเรื่องสำคัญกันดีกว่า")
        else:
            speak("สวัสดีครับ!")
    await asyncio.sleep(1)

# เริ่มต้นการทำงาน
if __name__ == "__main__":
    asyncio.run(main())
# talk_manager.py

import pygame
from gtts import gTTS
import os

# ฟังก์ชันพูด (TTS)
def speak(text):
    # เริ่ม pygame mixer เพื่อเล่นเสียง
    pygame.mixer.init()
    tts = gTTS(text=text, lang='th')  # ใช้ gTTS ในการสร้างเสียง
    tts.save("output.mp3")
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # รอให้เสียงเล่นเสร็จ
        pygame.time.Clock().tick(10)

# ฟังก์ชันตั้งโหมดพูด
def set_mode(new_mode):
    print(f"[🧠] เปลี่ยนโหมดพูดเป็น: {new_mode}")

# ฟังก์ชันตรวจสอบว่า AI ควรพูดหรือไม่
def should_talk(interval_sec=120):
    # ในที่นี้เราจะสมมติว่า AI ควรพูดทุก 2 นาที
    return True
