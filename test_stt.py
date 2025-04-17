import asyncio
from speech.stt_faster_whisper import transcribe_from_mic

async def main():
    text = await transcribe_from_mic()
    print("🎤 ได้ข้อความ:", text)

asyncio.run(main())
