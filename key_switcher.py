import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEYS = os.getenv("GEMINI_API_KEYS", "").split(",")
YOUTUBE_API_KEYS = os.getenv("YOUTUBE_API_KEYS", "").split(",")

def get_valid_gemini_key(index=0):
    if index >= len(GEMINI_API_KEYS):
        raise Exception("🚫 ไม่พบ Gemini API Key ที่ใช้ได้")
    key = GEMINI_API_KEYS[index].strip()
    if key:
        os.environ["GEMINI_API_KEY"] = key
        return key
    else:
        return get_valid_gemini_key(index + 1)

def get_valid_youtube_key(index=0):
    if index >= len(YOUTUBE_API_KEYS):
        raise Exception("🚫 ไม่พบ YouTube API Key ที่ใช้ได้")
    key = YOUTUBE_API_KEYS[index].strip()
    if key:
        os.environ["YOUTUBE_API_KEY"] = key
        return key
    else:
        return get_valid_youtube_key(index + 1)