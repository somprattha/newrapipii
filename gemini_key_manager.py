import os

GEMINI_KEYS = os.getenv("GEMINI_API_KEYS", "").split(",")
current_gemini_index = 0

def get_current_gemini_key():
    if not GEMINI_KEYS:
        return None
    return GEMINI_KEYS[current_gemini_index % len(GEMINI_KEYS)]

def switch_to_next_gemini_key():
    global current_gemini_index
    current_gemini_index += 1
    return get_current_gemini_key()
