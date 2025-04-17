
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from speech_to_text import transcribe_audio
from gemini_api_manager import ask_gemini
from tts_manager import speak_from_text

def listen_and_reply():
    print("[STT] 🎤 กำลังฟังเสียงจากไมโครโฟน...")
    text = transcribe_audio()
    if not text:
        return None
    print(f"[STT] ได้ข้อความ: {text}")

    # ส่งข้อความไปยัง Gemini Flash
    reply = ask_gemini(text)
    if reply:
        print(f"[Gemini] 🤖 ตอบกลับ: {reply}")
        return reply
    return None
