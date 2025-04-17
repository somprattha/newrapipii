import json
from datetime import datetime

LOG_FILE = "voice_chat_log.json"

def save_user_log(username, message):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            log = json.load(f)
    except:
        log = {}

    if username not in log:
        log[username] = []

    log[username].append({
        "timestamp": datetime.now().isoformat(),
        "message": message
    })

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)