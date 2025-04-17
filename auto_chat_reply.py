import time
from datetime import datetime
import random
import json
from fan_vip_manager import get_user_vip
from gacha_voice import get_lucky_voice
from multi_tts_engine import speak
from gemini_memory import chat_with_memory
from web_socket_overlay import send_vip_overlay

# -----------------------
# ระบบจำแฟนขาประจำ
# -----------------------
FAN_HISTORY_FILE = "fan_memory.json"
try:
    with open(FAN_HISTORY_FILE, "r", encoding="utf-8") as f:
        fan_memory = json.load(f)
except:
    fan_memory = {}

# -----------------------
# มุกสุ่มตอบกลับ
# -----------------------
JOKES = [
    "รู้อะไรมั้ย~ คุณน่ะ น่ารักที่สุดในแชทเลย! 💕",
    "จะว่าไป... วันนี้ทานข้าวหรือยังน้า~",
    "ถ้าคิดถึงราปิปี้เมื่อไหร่ ให้ส่งหัวใจมานะ~ 💖",
    "ราปิปี้ไม่ได้หยอกนะ... รักเลยต่างหาก~ 😳"
]

# -----------------------
# ระบบตอบกลับหลัก
# -----------------------
replied_users = {}

def save_memory():
    with open(FAN_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(fan_memory, f, indent=2, ensure_ascii=False)

def process_live_chat(user, message):
    global replied_users

    now = datetime.now()
    if user in replied_users and (now - replied_users[user]).seconds < 10:
        return
    replied_users[user] = now

    print(f"[👀 ข้อความจากแชท] {user}: {message}")
    
    # บันทึกประวัติแฟน
    if user not in fan_memory:
        fan_memory[user] = {
            "count": 1,
            "last_message": message
        }
    else:
        fan_memory[user]["count"] += 1
        fan_memory[user]["last_message"] = message
    save_memory()

    # ตรวจ VIP
    vip = get_user_vip(user)
    vip_icon = {
        "⭐": "⭐",
        "🌟": "🌟",
        "💖": "💖",
        "👑": "👑"
    }.get(vip, "")

    if fan_memory[user]["count"] % 7 == 0:
        msg = random.choice(JOKES)
        full = f"{user}{vip_icon}~ {msg}"
        speak(full)
        send_vip_overlay(user, msg, emoji="💬")
        return

    prompt = f"มีแฟนชื่อ {user}{vip_icon} พิมพ์ว่า: {message}\nกรุณาตอบกลับแบบ VTuber ช่างพูด หยอดเก่ง ปลอบใจเก่ง"
    try:
        reply = chat_with_memory(prompt)
        print(f"[🧠 AI ตอบ]: {reply}")
        speak(reply)
        send_vip_overlay(user, reply, emoji="✨")
    except Exception as e:
        print(f"[❌ ตอบกลับล้มเหลว]: {str(e)}")