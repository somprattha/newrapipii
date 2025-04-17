
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")

def transcribe_audio(duration=5, samplerate=16000):
    print("[STT] 🎧 กำลังฟัง...")
    try:
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()
        audio_data = np.squeeze(audio)

        segments, _ = model.transcribe(audio_data, beam_size=5)
        full_text = ""
        for segment in segments:
            full_text += segment.text.strip() + " "
        return full_text.strip()
    except Exception as e:
        print(f"[STT] ❌ Error: {e}")
        return ""
