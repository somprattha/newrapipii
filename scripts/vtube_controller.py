import asyncio
import websockets
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class VTubeStudioController:
    def __init__(self, uri="ws://localhost:8001"):
        self.uri = uri
        self.ws = None
        self.emotion_to_expression = {
            "happy": "微笑.exp3.json",
            "sad": "流泪.exp3.json",
            "angry": "生气.exp3.json",
            "surprised": "惊讶.exp3.json",
            "love": "爱心眼.exp3.json",
            "fan_girl": "星星眼.exp3.json",
            "pout": "歪嘴→.exp3.json",
            "pout_left": "←歪嘴.exp3.json",
            "blush": "脸红.exp3.json",
            "teary": "流泪.exp3.json",
            "smirk": "坏笑.exp3.json",
            "sleepy": "困.exp3.json",
            "cry_silent": "流泪.exp3.json",
            "tsundere_blush": "害羞.exp3.json",
            "jealous": "斜眼.exp3.json",
            "possessive": "歪嘴→.exp3.json",
            "super_shy": "害羞+脸红.exp3.json"
        }

    async def connect(self):
        self.ws = await websockets.connect(self.uri)
        logger.info("✅ เชื่อมต่อกับ VTube Studio แล้ว")

    async def close(self):
        if self.ws:
            await self.ws.close()
            logger.info("🛑 ปิดการเชื่อมต่อเรียบร้อย")

    async def set_expression(self, emotion_name: str):
        expression_file = self.emotion_to_expression.get(emotion_name)
        if not expression_file:
            logger.warning(f"⚠️ ไม่มีอารมณ์ชื่อ '{emotion_name}' ในแมป")
            return

        request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": f"set-expression-{emotion_name}",
            "messageType": "SetCurrentExpressionRequest",
            "data": {
                "expressionFile": expression_file
            }
        }

        await self.ws.send(json.dumps(request))
        response = await self.ws.recv()
        logger.info(f"🎭 ตั้งค่าอารมณ์ '{emotion_name}' ด้วยไฟล์ {expression_file} → ผลลัพธ์: {response}")

# 🧪 ตัวอย่างการใช้งาน
async def main():
    controller = VTubeStudioController()
    await controller.connect()

    # ทดสอบเปลี่ยนอารมณ์เป็น 'happy'
    await controller.set_expression("happy")

    await controller.close()

if __name__ == "__main__":
    asyncio.run(main())
