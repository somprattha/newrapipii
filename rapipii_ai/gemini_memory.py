
import json
import os
from datetime import datetime

LOG_FILE = "log_memory.json"

def log_and_remember(user_input, ai_reply):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "reply": ai_reply
    }

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except:
                logs = []

    logs.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

    print("[Memory] 🧠 จำไว้เรียบร้อยแล้ว~")

def chat_with_memory(user_input):
    print(f"[MemoryChat] 🤖 ประมวลผลคำถามพร้อมความจำ: {user_input}")
    return "รัปปี้จำได้เลย~ พี่เคยพูดแบบนี้มาก่อนแน่ๆ~"
