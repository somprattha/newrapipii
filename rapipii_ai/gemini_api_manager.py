
import aiohttp
import asyncio
import random
from datetime import datetime, timedelta
import pytz

THAI_TZ = pytz.timezone('Asia/Bangkok')

class GeminiClient:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.api_key = "YOUR_GEMINI_API_KEY"
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
        self.daily_quota = 1500
        self.request_count = 0
        self.last_reset = self.get_bangkok_day_start()

    def get_bangkok_day_start(self):
        now = datetime.now(THAI_TZ)
        return now.replace(hour=7, minute=0, second=0, microsecond=0)

    def check_and_reset_quota(self):
        now = datetime.now(THAI_TZ)
        if now >= self.last_reset + timedelta(days=1):
            self.request_count = 0
            self.last_reset = self.get_bangkok_day_start()

    async def send_message(self, text):
        self.check_and_reset_quota()

        if self.request_count >= self.daily_quota:
            return "ขออภัย วันนี้ครบจำนวนคำขอสูงสุดแล้ว กรุณารอพรุ่งนี้"

        await asyncio.sleep(random.uniform(4, 6))  # Delay 4-6 วินาที (15 RPM)

        payload = {
            "contents": [{"parts": [{"text": text}]}]
        }

        try:
            async with self.session.post(self.api_url, json=payload) as resp:
                data = await resp.json()
                self.request_count += 1
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"❌ Gemini error: {e}"

    async def close(self):
        await self.session.close()
