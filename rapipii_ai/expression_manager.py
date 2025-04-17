
import requests
import random
import re

VTS_API_URL = "http://localhost:8001"  # เปลี่ยนตาม config ของ VTube Studio

EMOTION_KEYWORDS = {
    "happy": ["ดีใจ", "เยี่ยม", "ขอบคุณ", "ฮา", "555", "เก่งมาก", "ดีมาก"],
    "sad": ["เสียใจ", "แย่จัง", "เศร้า", "ร้องไห้", "เหงา"],
    "angry": ["โกรธ", "โมโห", "ไม่พอใจ", "บ้าไปแล้ว"],
    "surprised": ["จริงเหรอ", "ห๊ะ", "เหรอ", "โอ้โห", "ว้าว"],
    "neutral": []  # fallback
}

EXPRESSION_MAP = {
    "happy": "Smile",
    "sad": "Sad",
    "angry": "Angry",
    "surprised": "Surprised",
    "neutral": "Idle"
}

def detect_emotion(text):
    for emotion, keywords in EMOTION_KEYWORDS.items():
        for word in keywords:
            if re.search(rf"{re.escape(word)}", text, re.IGNORECASE):
                return emotion
    return "neutral"

def trigger_expression(expression):
    exp_name = EXPRESSION_MAP.get(expression, "Idle")
    payload = {
        "messageType": "HotkeyTriggerRequest",
        "data": {
            "hotkeyID": exp_name
        }
    }
    try:
        requests.post(VTS_API_URL, json=payload, timeout=1)
        print(f"🌀 Expression triggered: {exp_name}")
    except requests.RequestException as e:
        print(f"❌ Failed to trigger expression: {e}")

def process_text_for_expression(text):
    emotion = detect_emotion(text)
    trigger_expression(emotion)
