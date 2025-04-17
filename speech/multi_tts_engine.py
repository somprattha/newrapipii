
import os
import random
import requests
import json
from datetime import datetime
from google.cloud import texttospeech
from gtts import gTTS
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

QUOTA_FILE = "tts_quota.json"
AZURE_KEY = os.getenv("AZURE_TTS_KEY")
AZURE_REGION = os.getenv("AZURE_TTS_REGION")
AZURE_ENDPOINT = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"

GOOGLE_CLIENT = texttospeech.TextToSpeechClient()

QUOTAS = {
    "azure_tts": 500_000,
    "google_neural2_tts": 1_000_000,
    "google_wavenet_tts": 1_000_000,
    "google_standard_tts": 4_000_000,
    "gtts_fallback": float('inf'),
    "edge_fallback": float('inf')
}

AVAILABLE_GOOGLE_VOICES = []

def fetch_google_voices():
    global AVAILABLE_GOOGLE_VOICES
    if not AVAILABLE_GOOGLE_VOICES:
        response = GOOGLE_CLIENT.list_voices()
        AVAILABLE_GOOGLE_VOICES = [voice.name for voice in response.voices if voice.language_codes and "th-TH" in voice.language_codes]
    return AVAILABLE_GOOGLE_VOICES

def validate_google_voice(voice_name):
    return voice_name in fetch_google_voices()

def count_characters(text):
    return len(text)

def should_reset_quota():
    now = datetime.now()
    return now.day == 1 and now.hour >= 7

def load_quota():
    if not os.path.exists(QUOTA_FILE):
        return {k: 0 for k in QUOTAS.keys()}
    with open(QUOTA_FILE, 'r') as f:
        return json.load(f)

def save_quota(quota):
    with open(QUOTA_FILE, 'w') as f:
        json.dump(quota, f, indent=2)

def reset_quota_if_needed():
    if should_reset_quota():
        print("♻️ รีเซ็ตโควต้า TTS รายเดือน (Auto)")
        save_quota({k: 0 for k in QUOTAS.keys()})

def update_quota(provider_name, count):
    quota = load_quota()
    quota[provider_name] = quota.get(provider_name, 0) + count
    save_quota(quota)

def is_quota_exceeded(provider_name):
    quota = load_quota()
    return quota.get(provider_name, 0) >= QUOTAS[provider_name] * 0.99

def azure_tts(text):
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
        "User-Agent": "RapheepeeAI"
    }
    ssml = f"""
    <speak version='1.0' xml:lang='th-TH'>
        <voice xml:lang='th-TH' xml:gender='Female' name='th-TH-PremwadeeNeural'>
            {text}
        </voice>
    </speak>
    """
    response = requests.post(AZURE_ENDPOINT, headers=headers, data=ssml.encode('utf-8'))
    if response.status_code == 200:
        update_quota("azure_tts", count_characters(text))
        return response.content
    else:
        raise Exception(f"Azure TTS failed: {response.status_code} {response.text}")

def google_neural2_tts(text):
    voice_name = "th-TH-Neural2-A"
    if not validate_google_voice(voice_name):
        raise ValueError(f"Invalid Neural2 voice name: {voice_name}")
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="th-TH", name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = GOOGLE_CLIENT.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    update_quota("google_neural2_tts", count_characters(text))
    return response.audio_content

def google_wavenet_tts(text):
    voice_name = "th-TH-Wavenet-A"
    if not validate_google_voice(voice_name):
        raise ValueError(f"Invalid Wavenet voice name: {voice_name}")
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="th-TH", name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = GOOGLE_CLIENT.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    update_quota("google_wavenet_tts", count_characters(text))
    return response.audio_content

def google_standard_tts(text):
    voice_name = "th-TH-Standard-A"
    if not validate_google_voice(voice_name):
        raise ValueError(f"Invalid Standard voice name: {voice_name}")
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="th-TH", name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = GOOGLE_CLIENT.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    update_quota("google_standard_tts", count_characters(text))
    return response.audio_content

def gtts_fallback(text):
    tts = gTTS(text=text, lang='th')
    tmp_path = "gtts_fallback.mp3"
    tts.save(tmp_path)
    update_quota("gtts_fallback", count_characters(text))
    return Path(tmp_path).read_bytes()

def edge_fallback(text):
    update_quota("edge_fallback", count_characters(text))
    return gtts_fallback(text)

def speak(text, output_file="output.mp3"):
    reset_quota_if_needed()
    providers = [
        azure_tts,
        google_neural2_tts,
        google_wavenet_tts,
        google_standard_tts,
        gtts_fallback,
        edge_fallback
    ]
    for provider in providers:
        if is_quota_exceeded(provider.__name__):
            print(f"⛔ Quota exceeded: {provider.__name__}")
            continue
        try:
            print(f"🔊 Trying: {provider.__name__}")
            audio = provider(text)
            with open(output_file, "wb") as f:
                f.write(audio)
            print(f"✅ Success: {provider.__name__}")
            return
        except Exception as e:
            print(f"⚠️ Failed {provider.__name__}: {e}")
    print("❌ All TTS providers failed.")
