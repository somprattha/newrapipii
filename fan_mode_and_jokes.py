import random
from multi_tts_engine import speak
from web_socket_overlay import send_vip_overlay

# ==============================
# โหมดแฟนขาประจำ
# ==============================

regular_fans = ["พี่", "มิกิ", "มายด์", "คุณต้น"]  # เพิ่มชื่อแฟนประจำตรงนี้

def is_regular_fan(name):
    return name in regular_fans

def greet_regular_fan(name):
    if is_regular_fan(name):
        line = f"อ๊า~ {name} มาแล้ว~ วันนี้ราปิปี้รอเลยนะ~ 💖"
        speak(line)
        send_vip_overlay(name, line, emoji="🐰")
        return True
    return False

# ==============================
# ระบบสุ่มมุก
# ==============================

joke_list = [
    "เมื่อไหร่เราจะได้เป็นแฟนกันแบบจริงจังซะทีล่ะ~ 😳",
    "อยากเป็นนาฬิกา... จะได้อยู่ทุกเวลาใกล้ใจคุณ~ 🕒💕",
    "ราปิปี้ไม่ใช่น้ำตาล แต่ก็หวานไม่แพ้นะ~ 🍬",
    "อ๊ะ! หัวใจร่วง~ ช่วยเก็บให้หน่อยสิ~ 💓"
]

def tell_random_joke():
    line = random.choice(joke_list)
    speak(line)
    send_vip_overlay("ราปิปี้", line, emoji="🎀")

# ==============================
# ระบบหลอกดุแล้วแกล้งง้อ
# ==============================

def fake_angry_and_apologize(name):
    speak(f"{name}! ทำไมดื้อนักน้า~! 😠")
    time.sleep(2)
    speak(f"แง... ขอโทษนะ~ ราปิปี้ไม่ได้ตั้งใจดุจริงๆ~ อย่าหนีไปนะ~ 🥺")
    send_vip_overlay(name, "ขอโทษน้า~ มาง้อแล้ว~ 💞", emoji="💘")