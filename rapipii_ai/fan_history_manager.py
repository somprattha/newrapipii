# fan_history_manager.py — จัดการประวัติแฟนคลับย้อนหลัง
import json, datetime

HISTORY_FILE = "fan_history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_history(data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_fan(user, action="chat"):
    data = load_history()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if user not in data:
        data[user] = {
            "first_seen": now,
            "last_active": now,
            "chat_count": 1,
            "donate_count": 0
        }
    else:
        data[user]["last_active"] = now
        if action == "chat":
            data[user]["chat_count"] += 1
        elif action == "donate":
            data[user]["donate_count"] += 1
    save_history(data)

def get_fan_summary(user):
    data = load_history()
    if user in data:
        f = data[user]
        return f"🧾 คุณเคยแชท {f['chat_count']} ครั้ง / เข้ามาครั้งแรกเมื่อ {f['first_seen']}"
    else:
        return "ยังไม่มีประวัตินะ ลองแชทดูสิ~"