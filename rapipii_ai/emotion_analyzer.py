
def analyze_emotion(text):
    text = text.lower()
    if any(word in text for word in ["ดีใจ", "เย้", "สุดยอด", "ตื่นเต้น"]):
        return "happy"
    elif any(word in text for word in ["เสียใจ", "เศร้า", "ร้องไห้"]):
        return "sad"
    elif any(word in text for word in ["โกรธ", "โมโห", "เดือด"]):
        return "angry"
    elif any(word in text for word in ["ตกใจ", "ว้าว", "จริงดิ", "ไม่อยากเชื่อ"]):
        return "surprised"
    elif any(word in text for word in ["รัก", "คิดถึง", "เขิน", "อ้อน"]):
        return "love"
    elif any(word in text for word in ["เบื่อ", "ไม่สนใจ", "เฉยๆ"]):
        return "neutral"
    else:
        return "neutral"
def detect_emotion(text):
    emotion_map = {
        "งอน": "pout",
        "เขิน": "blush",
        "หึง": "jealous",
        "ง่วง": "sleepy",
        "ร้องไห้": "cry_silent",
        "เขินจัดขั้นสุด": "super_shy",  # เพิ่มใหม่
        "ร้องไห้สะอื้น": "teary",  # เพิ่มใหม่
        "ยิ้มมุมปากแบบร้าย ๆ": "smirk"  # เพิ่มใหม่
    }

    # ตรวจจับคำสำคัญในข้อความและแมปไปที่ Expression
    for keyword, expression in emotion_map.items():
        if keyword in text:
            return expression
    return "default"  # ถ้าไม่พบคำไหนใช้ default
