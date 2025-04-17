from emotion_analyzer import detect_emotion

def set_expression(expression):
    print(f"[VTS] 🖼️ ตั้ง Expression เป็น: {expression}")
    # ใส่โค้ดจริงเพื่อสั่ง VTube Studio ผ่าน API

def update_expression_based_on_chat(chat_message):
    emotion = detect_emotion(chat_message)
    set_expression(emotion)