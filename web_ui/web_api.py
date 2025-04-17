from flask import Flask, request, send_file
from core import tts_manager
import os

app = Flask(__name__)

@app.route("/api/tts/preview", methods=["POST"])
def tts_preview():
    data = request.json
    model = data.get("model", "azure")
    pitch = float(data.get("pitch", 0))
    rate = float(data.get("rate", 1.0))
    text = data.get("text", "สวัสดีค่ะ ราปิปี้นะคะ~")

    try:
        audio_path = tts_manager.speak_with_settings(
            text, model=model, pitch=pitch, rate=rate, preview=True
        )
        # คัดลอกไฟล์มาไว้ static เพื่อให้ web เล่นได้
        os.makedirs("static", exist_ok=True)
        static_path = "static/preview_audio.mp3"
        os.replace(audio_path, static_path)
        return "✅ เสียงตัวอย่างถูกสร้างแล้ว~"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
