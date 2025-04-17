import edge_tts
import asyncio
import os

def run_edge_tts(text, voice="th-TH-NarisaNeural"):
    async def run():
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save("output.mp3")
        os.system("start output.mp3")
    asyncio.run(run())