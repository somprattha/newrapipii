import sounddevice as sd
import numpy as np
import queue
import asyncio
from faster_whisper import WhisperModel

AUDIO_DEVICE_NAME = "AMD Streaming Audio Device"
SAMPLE_RATE = 16000
DURATION = 4

model = WhisperModel("small", compute_type="auto")
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

def get_device_index():
    devices = sd.query_devices()
    for idx, dev in enumerate(devices):
        if AUDIO_DEVICE_NAME in dev['name']:
            return idx
    raise RuntimeError(f"⚠️ ไม่พบอุปกรณ์เสียงชื่อ '{AUDIO_DEVICE_NAME}'")

async def transcribe_microphone():
    device_index = get_device_index()
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=audio_callback, device=device_index):
        print(f"🎧 กำลังฟังจากไมโครโฟน: '{AUDIO_DEVICE_NAME}'...")
        await asyncio.sleep(DURATION)

        frames = []
        while not audio_queue.empty():
            frames.append(audio_queue.get())

        if not frames:
            print("⚠️ ไม่พบข้อมูลเสียง")
            return ""

        audio = np.concatenate(frames, axis=0).flatten()
        audio = audio.astype(np.float32)

        print("🧠 แปลงเสียงเป็นข้อความ...")
        segments, _ = model.transcribe(audio, beam_size=5)

        full_text = " ".join([seg.text.strip() for seg in segments])
        return full_text.strip()

async def transcribe_from_mic():
    return await transcribe_microphone()
