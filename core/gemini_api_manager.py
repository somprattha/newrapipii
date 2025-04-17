
import json
import os
import random
import time
from datetime import datetime, timedelta
import google.generativeai as genai

KEY_FILE = "gemini_keys.json"
QUOTA_FILE = "gemini_quota.json"
MODEL = "gemini-2.0-flash"
MAX_RPD = 1500
MAX_RPM = 15

# โหลดคีย์หลายตัว
with open(KEY_FILE, "r") as f:
    ALL_KEYS = json.load(f)["api_keys"]

# โหลดหรือเริ่ม quota log
if os.path.exists(QUOTA_FILE):
    with open(QUOTA_FILE, "r") as f:
        usage = json.load(f)
else:
    usage = {key: {"rpd": 0, "rpm": [], "last_reset": str(datetime.utcnow())} for key in ALL_KEYS}

# รีเซ็ตประจำวัน UTC 00:00
now = datetime.utcnow()
for key, data in usage.items():
    last_reset = datetime.fromisoformat(data["last_reset"])
    if now.date() > last_reset.date():
        usage[key] = {"rpd": 0, "rpm": [], "last_reset": now.isoformat()}

# ฟังก์ชันเลือกคีย์แบบหมุนอัตโนมัติ
current_key_index = 0

def rotate_key():
    global current_key_index
    for i in range(len(ALL_KEYS)):
        key = ALL_KEYS[current_key_index]
        q = usage[key]
        if q["rpd"] < MAX_RPD and len(q["rpm"]) < MAX_RPM:
            return key
        current_key_index = (current_key_index + 1) % len(ALL_KEYS)
    raise Exception("❌ เกินโควต้า Gemini ทุก key แล้ว")

def record_usage(key):
    usage[key]["rpd"] += 1
    usage[key]["rpm"] = [t for t in usage[key]["rpm"] if time.time() - t < 60]
    usage[key]["rpm"].append(time.time())
    with open(QUOTA_FILE, "w") as f:
        json.dump(usage, f, indent=2)

def ask_gemini(prompt):
    key = rotate_key()
    genai.configure(api_key=key)
    model = genai.GenerativeModel(MODEL)
    chat = model.start_chat()
    response = chat.send_message(prompt)
    record_usage(key)
    return response.text.strip()
