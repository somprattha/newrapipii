# quiz_game.py
import random

quiz_bank = [
    {"question": "วันนี้อยากกินอะไรที่สุด?", "choices": ["🍜 ราเมน", "🍕 พิซซ่า", "🍰 เค้ก"], "answer": "🍜 ราเมน"},
    {"question": "คุณชอบฤดูไหนมากที่สุด?", "choices": ["❄️ หน้าหนาว", "☀️ หน้าร้อน", "🌧️ หน้าฝน"], "answer": "❄️ หน้าหนาว"}
]

def get_random_quiz():
    return random.choice(quiz_bank)