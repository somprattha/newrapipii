from gtts import gTTS
import os

def gtts_fallback(text):
    tts = gTTS(text=text, lang="th")
    tts.save("output.mp3")
    os.system("start output.mp3")