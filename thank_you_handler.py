import random
from multi_tts_engine import speak
from gacha_voice import get_lucky_voice
from web_socket_overlay import send_vip_overlay
from fan_vip_manager import get_user_vip, add_coin

def handle_donation_event(event_type, username, vip_level=None):
    add_coin(username, amount=30 if event_type == "donation" else 10)
    true_level = vip_level or get_user_vip(username)
    thank_message = get_lucky_voice(true_level)
    full_text = f"ขอบคุณ {username} มากๆ นะ~ {thank_message}"
    speak(full_text)
    send_vip_overlay(username, thank_message, true_level)
    print(f"[{event_type}] Thanked {username} ({true_level}): {thank_message}")