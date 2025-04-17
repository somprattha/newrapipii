# chat_recall.py
import json
from datetime import datetime, timedelta

def load_chat_memory():
    try:
        with open("chat_memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def recall_yesterday_message(user):
    memory = load_chat_memory()
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    return memory.get(user, {}).get(yesterday, "เมื่อวานเราไม่ได้คุยกันเลยน้า~")

def save_chat(user, text):
    memory = load_chat_memory()
    today = datetime.now().strftime("%Y-%m-%d")
    memory.setdefault(user, {})[today] = text
    with open("chat_memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)