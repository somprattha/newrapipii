import os
import time
import google.generativeai as genai
from faster_whisper import WhisperModel
from playsound import playsound
from tts_fallback import speak  # ใช้ fallback TTS อัตโนมัติ

# ✅ รองรับการสลับหลาย API Key อัตโนมัติ
API_KEYS = [
    os.getenv("GEMINI_API_KEY1"),
    os.getenv("GEMINI_API_KEY2"),
    os.getenv("GEMINI_API_KEY3"),
    os.getenv("GEMINI_API_KEY4"),
]

class GeminiManager:
    def __init__(self):
        self.api_keys = [k for k in API_KEYS if k]  # กรองคีย์ที่ไม่ใช้งานออก
        self.index = 0
        self.model_name = 'models/gemini-2.0-flash'
        self._configure()

    def _configure(self):
        genai.configure(api_key=self.api_keys[self.index])
        self.model = genai.GenerativeModel(self.model_name)

    def rotate_key(self):
        self.index = (self.index + 1) % len(self.api_keys)
        self._configure()

    def ask_gemini(self, prompt):
        for _ in range(len(self.api_keys)):
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                print(f"[❌] Gemini Key {self.index+1} Error:", e)
                self.rotate_key()
        return "ขออภัยค่ะ ระบบตอบกลับไม่สำเร็จในตอนนี้"

# ✅ ใช้แบบโมดูลหรือ import
gemini_instance = GeminiManager()

def ask_gemini(prompt):
    return gemini_instance.ask_gemini(prompt)

# ✅ STT ร่วมกับ WhisperModel
model = WhisperModel("small", device="cpu", compute_type="int8")

def speech_to_text():
    print("🎙️ กำลังฟังเสียง... พูดใส่ไมค์เลยนะ")
    os.system("arecord -d 5 -f cd -t wav -r 16000 -c 1 input.wav")  # สำหรับ Linux (หากใช้ Windows เปลี่ยน method)
    segments, _ = model.transcribe("input.wav", beam_size=5)
    return " ".join([seg.text for seg in segments])

# ✅ ใช้สำหรับรันแยกไฟล์
if __name__ == "__main__":
    text = speech_to_text()
    print("💬 คำพูดที่ถอดเสียงได้:", text)

    response = ask_gemini(text)
    print("🤖 คำตอบจากราปิปี้:", response)

    audio_file = speak(response)
    if audio_file:
        playsound(audio_file)
