import asyncio
import logging
from vtube_controller import VTubeController
from rapipii_core import RapipiiAI
from emotion_analyzer import EmotionAnalyzer
from stt_faster_whisper import transcribe_audio
from tts_manager import speak
from gemini_api_manager import query_gemini

# ตั้งค่า Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    # เริ่มต้น RapipiiAI
    rapipii = RapipiiAI()

    # เริ่มต้นการเชื่อมต่อ VTubeStudio
    vtube_controller = VTubeController()
    await vtube_controller.connect()

    # เริ่มต้น Emotion Analyzer
    emotion_analyzer = EmotionAnalyzer()

    # การฟังเสียงจากไมโครโฟน
    audio_result = transcribe_audio()  # ฟังก์ชันนี้จะใช้ faster-whisper
    logger.info(f"ผลการแปลงเสียง: {audio_result}")

    # วิเคราะห์อารมณ์จากเสียง
    emotion = emotion_analyzer.analyze_emotion(audio_result)
    logger.info(f"อารมณ์ที่วิเคราะห์ได้: {emotion}")

    # สั่ง RapipiiAI แสดงอารมณ์ตามการวิเคราะห์
    rapipii.display_expression(emotion)

    # คำถามกับ Gemini (ใช้ได้สำหรับข้อมูลเสริม)
    gemini_response = query_gemini(audio_result)
    logger.info(f"คำตอบจาก Gemini: {gemini_response}")

    # พูดตอบกลับจากการวิเคราะห์ (สามารถเพิ่มระบบ TTS ได้)
    speak(f"ผลการวิเคราะห์อารมณ์: {emotion}")

    # จบการเชื่อมต่อ
    await vtube_controller.close()
    logger.info("🛑 ปิดการเชื่อมต่อเรียบร้อย")

# รันโปรแกรมหลัก
if __name__ == "__main__":
    asyncio.run(main())
