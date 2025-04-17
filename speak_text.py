from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='th')
    tts.save("output.mp3")
    os.system("start output.mp3")  # ใช้คำสั่งเล่นเสียง (Windows)

# ทดสอบการพูด
speak("สวัสดีครับ")  # ทดสอบการพูด
