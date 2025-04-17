import random
from multi_tts_engine import speak
from web_socket_overlay import send_vip_overlay

# ============================
# 🌟 Rapipii Surprise Time!
# ============================

surprise_lines = [
    "ใครที่อยู่ถึงตอนนี้ รู้ไหมว่าคุณคือแฟนที่ราปิปี้รักที่สุดเลย~ 💖",
    "เซอร์ไพรส์~! วันนี้มีเสียงพิเศษมาให้คุณเท่านั้นเลย~ 🎁",
    "แอบกระซิบเบาๆ... ราปิปี้มีหัวใจดวงเดียว และมอบให้คุณ~ 🥺",
    "คุณได้ Lucky Voice จากราปิปี้~ ยินดีด้วยนะคะ! 💫"
]

def rapipii_surprise():
    line = random.choice(surprise_lines)
    speak(line)
    send_vip_overlay("ราปิปี้", line, emoji="🎉")

# ============================
# 🎤 คำพูดก่อนจบไลฟ์
# ============================

farewell_lines = [
    "ถึงเวลาที่ราปิปี้ต้องไปพักแล้ว ขอบคุณที่อยู่เป็นเพื่อนกันนะ~ 🌙",
    "ฝันดีนะคะทุกคน~ เจอกันใหม่ในสตรีมหน้า~ 💕",
    "แม้จะไม่ได้อยู่ตรงหน้า แต่ราปิปี้จะคิดถึงทุกคนเสมอ~ 🐰✨",
    "ก่อนจากกันคืนนี้ ราปิปี้ขอส่งพลังใจให้เต็มที่เลย~ 💖"
]

def rapipii_farewell():
    line = random.choice(farewell_lines)
    speak(line)
    send_vip_overlay("ราปิปี้", line, emoji="🌙")