# chat_flair.py — คำตอบแนวหยอด/งอน/มุข
import random

def get_flirty_reply():
    return random.choice([
        "พูดแบบนี้ ระวังจะตกหลุมรักเค้านะ~ 💘",
        "วันนี้ดูน่ารักจังเลยน้า~ หรือว่าเราคิดไปเอง 😳",
        "อยากให้ราปิปี้อยู่ข้าง ๆ มั้ย~ 🐰"
    ])

def get_tsundere_reply():
    return random.choice([
        "ไม่ได้อยากตอบหรอกนะ... แต่ก็เอาเถอะ! 😤",
        "หืมม~ มาทักซะช้าเลยน้า~",
        "ใครเค้าคิดถึงกันเล่า! ก็แค่... เผลอคิดถึงนิดเดียวเอง..."
    ])

def get_joke_reply():
    return random.choice([
        "มีมุขนะ... ทำไมไก่ถึงไม่ข้ามถนน? เพราะมันขี้เกียจ 🐔",
        "ตกลงเรามีใจให้กัน หรือแค่หลงทางมา~ 🤪",
        "เค้าคิดเลขไม่เก่ง... แต่เค้าคิดถึงเก่งนะ~ 😝"
    ])