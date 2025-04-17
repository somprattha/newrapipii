
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from tts_manager import stop_speaking
from gemini_api_manager import ask_gemini
from tts_manager import speak
from mic_device_config import get_default_microphone

model = WhisperModel("small", device="cpu", compute_type="int8")

def mic_command_listener():
    default_mic = get_default_microphone()
    if not default_mic:
        print("[MIC] ❌ ไม่พบไมโครโฟนที่จะใช้")
        return

    samplerate = 16000
    duration = 5  # ระยะเวลาที่ฟังต่อรอบ (วินาที)
    print(f"[MIC] ✅ เริ่มฟังจากไมค์: {default_mic}")

    while True:
        try:
            print("[MIC] 🎙️ ฟังเสียง...")
            audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
            sd.wait()
            audio_data = np.squeeze(audio)

            segments, _ = model.transcribe(audio_data, beam_size=5)
            for segment in segments:
                text = segment.text.strip()
                if text:
                    print(f"[🎤] ได้ยินว่า: {text}")
                    stop_speaking()
                    response = ask_gemini(text)
                    if response:
                        print(f"[Gemini] 🤖 ตอบว่า: {response}")
                        speak(response)
        except KeyboardInterrupt:
            print("[MIC] ❌ หยุดฟัง (KeyboardInterrupt)")
            break
        except Exception as e:
            print(f"[MIC] ❌ Error: {e}")
