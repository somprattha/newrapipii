# thank_you_vip.py — พูดขอบคุณแฟนระดับ VIP ด้วยเสียงสุ่มแนวพิเศษ
from gacha_voice import get_lucky_voice
from multi_tts_engine import speak

def thank_vip(username, vip_level="⭐"):
    message = get_lucky_voice(vip_level)
    full = f"ขอบคุณ {username} มากๆ เลยนะ~ {message}"
    speak(full)