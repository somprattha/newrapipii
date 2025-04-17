import os
import json
import asyncio
from datetime import datetime
from gtts import gTTS
import edge_tts
import subprocess
import tempfile
from pydub import AudioSegment
from pydub.playback import play

# === CONFIG ===
LOG_PATH = "logs/tts_quota_log.json"
AUDIO_OUTPUT_PATH = "output_audio.wav"
DEVICE_NAME = "CABLE Input (VB-Audio Virtual Cable)"

# === LIMITS ===
QUOTA_LIMITS = {
    "google_chirp3": 1_000_000,
    "azure": 500_000,
    "google_standard": 4_000_000,
    "google_neural2": 1_000_000
}

# === INIT LOG ===
def load_quota_log():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "google_chirp3": 0,
            "azure": 0,
            "google_standard": 0,
            "google_neural2": 0,
            "last_reset": None
        }

def save_quota_log(log):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f)

def reset_quota_if_needed(log):
    now = datetime.utcnow()
    today = now.strftime("%Y-%m-%d")
    if log["last_reset"] != today:
        log["google_chirp3"] = 0
        log["azure"] = 0
        log["google_standard"] = 0
        log["google_neural2"] = 0
        log["last_reset"] = today
        save_quota_log(log)

# === CLEAN TEXT ===
def clean_text(text):
    import re
    return re.sub(r'[^\w\s฀-๿]', '', text)

# === ERROR LOGGING ===
def log_error(service_name, error_message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/tts_error_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} - {service_name}: {error_message}\n")

# === SPEAK ===
def speak(text):
    log = load_quota_log()
    reset_quota_if_needed(log)
    text = clean_text(text)

    print(f"💬 พูดว่า: {text}")

    # === Try Google Chirp3 HD ===
    if log["google_chirp3"] < QUOTA_LIMITS["google_chirp3"] * 0.99:
        success = generate_google_chirp3(text)
        if success:
            log["google_chirp3"] += len(text.split())
            save_quota_log(log)
            return

    # === Try Azure TTS ===
    if log["azure"] < QUOTA_LIMITS["azure"] * 0.99:
        success = generate_azure_tts(text)
        if success:
            log["azure"] += len(text.split())
            save_quota_log(log)
            return

    # === Try Google Neural2 TTS ===
    if log["google_neural2"] < QUOTA_LIMITS["google_neural2"] * 0.99:
        success = generate_google_neural2_tts(text)
        if success:
            log["google_neural2"] += len(text.split())
            save_quota_log(log)
            return

    # === Try Edge TTS ===
    success = generate_edge_tts(text)
    if success:
        return

    # === Try Google Standard TTS ===
    if log["google_standard"] < QUOTA_LIMITS["google_standard"] * 0.99:
        success = generate_google_standard_tts(text)
        if success:
            log["google_standard"] += len(text.split())
            save_quota_log(log)
            return

    # === Fallback gTTS ===
    generate_gtts(text)

# === Generate Google Chirp3 HD TTS ===
def generate_google_chirp3(text):
    try:
        print("🔊 Google Chirp3 HD:", text)
        # Add your actual Google API TTS logic here
        return False
    except Exception as e:
        log_error("google_chirp3", str(e))
        return False

# === Generate Azure TTS ===
def generate_azure_tts(text):
    try:
        print("🔊 Azure TTS:", text)
        # Replace with your actual Azure TTS API logic
        return False
    except Exception as e:
        log_error("azure", str(e))
        return False

# === Generate Google Neural2 TTS ===
def generate_google_neural2_tts(text):
    try:
        print("🔊 Google Neural2 TTS:", text)
        # Replace with your actual Google Neural2 TTS API logic
        return False
    except Exception as e:
        log_error("google_neural2", str(e))
        return False

# === Generate Edge TTS ===
def generate_edge_tts(text):
    try:
        communicate = edge_tts.Communicate(text=text, voice="th-TH-PremwadeeNeural")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            out_path = f.name
        asyncio.run(communicate.save(out_path))
        play_audio(out_path)
        return True
    except Exception as e:
        log_error("edge_tts", str(e))
        return False

# === Generate Google Standard TTS ===
def generate_google_standard_tts(text):
    try:
        print("🔊 Google Standard TTS:", text)
        # Replace with your actual Google Standard API TTS logic
        return False
    except Exception as e:
        log_error("google_standard", str(e))
        return False

# === Generate gTTS Fallback ===
def generate_gtts(text):
    try:
        print("🔊 gTTS:", text)
        tts = gTTS(text=text, lang='th')
        temp_path = "temp_gtts.mp3"
        tts.save(temp_path)
        play_audio(temp_path)
        os.remove(temp_path)
    except Exception as e:
        print("⚠️ gTTS failed:", e)

# === Play Audio ===
def play_audio(filepath):
    try:
        audio = AudioSegment.from_file(filepath)
        audio.export(AUDIO_OUTPUT_PATH, format="wav")
        subprocess.call(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", "-device", DEVICE_NAME, AUDIO_OUTPUT_PATH])
    except Exception as e:
        print(f"⚠️ Failed to play audio: {e}")
