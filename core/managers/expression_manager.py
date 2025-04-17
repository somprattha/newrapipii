import random
from core.vtube.vtube_controller import VTubeController

class ExpressionManager:
    def __init__(self):
        self.vtube = VTubeController()

    async def safe_set_expression(self, expression: str):
        try:
            await self.vtube.set_expression(expression)
        except Exception as e:
            print(f"[ExpressionManager] Failed to set expression: {e}")

    async def analyze_and_set(self, text: str, audio_path: str = None):
        # 🔍 วิเคราะห์อารมณ์จากข้อความ
        expression = self.detect_expression_from_text(text)

        # ✅ ส่งไป VTube Studio
        await self.safe_set_expression(expression)

    def detect_expression_from_text(self, text: str) -> str:
        # 🌈 ตัวอย่าง logic เบื้องต้น (สามารถแทนที่ด้วย AI หรือโมเดลได้ภายหลัง)
        text = text.lower()
        if any(word in text for word in ["ขอบคุณ", "ขอบใจ", "รัก", "เย้", "สุดยอด", "ดีใจ", "ติดตาม"]):
            return "joy"
        elif any(word in text for word in ["ห่วงใย", "เป็นห่วง", "น่ารัก", "อบอุ่น"]):
            return "gentle"
        elif any(word in text for word in ["เศร้า", "เสียใจ", "ขอโทษ"]):
            return "sad"
        elif any(word in text for word in ["โกรธ", "โมโห"]):
            return "angry"
        else:
            return random.choice(["neutral", "smile"])  # default
