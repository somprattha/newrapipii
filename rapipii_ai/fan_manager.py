import json
from datetime import datetime, timedelta
from core.talk_manager import speak
import pytz

FAN_MEMORY_PATH = "data/fan_return_memory.json"
ANNIVERSARY_THRESHOLDS = [7, 30, 90]  # วันครบรอบ

def load_memory():
    try:
        with open(FAN_MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(FAN_MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def on_fan_message(username):
    now = datetime.now(pytz.timezone("Asia/Bangkok"))
    data = load_memory()
    user_data = data.get(username)

    if not user_data:
        user_data = {
            "last_seen": now.strftime("%Y-%m-%d %H:%M:%S"),
            "first_seen": now.strftime("%Y-%m-%d %H:%M:%S")
        }
        data[username] = user_data
        save_memory(data)
        return

    last_seen = datetime.strptime(user_data["last_seen"], "%Y-%m-%d %H:%M:%S")
    first_seen = datetime.strptime(user_data["first_seen"], "%Y-%m-%d %H:%M:%S")
    days_absent = (now - last_seen).days
    days_since_first = (now - first_seen).days

    # พูดปลอบใจ
    if days_absent >= 3:
        speak(f"คุณ {username} หายไปตั้ง {days_absent} วันแน่ะ~ ราปิปี้ดีใจมากที่คุณกลับมานะคะ 💗")

    # วันครบรอบ
    for day in ANNIVERSARY_THRESHOLDS:
        if days_since_first == day:
            speak(f"วันนี้เป็นวันครบรอบ {day} วัน ที่ {username} มาหาราปิปี้~! ขอบคุณที่อยู่ด้วยกันนะคะ~ 🎉🐰")
            break

    # อัปเดต
    user_data["last_seen"] = now.strftime("%Y-%m-%d %H:%M:%S")
    data[username] = user_data
    save_memory(data)
