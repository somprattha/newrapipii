import websockets
import json
import uuid
import logging
import sys
import asyncio
from pathlib import Path
from typing import Optional

# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("vtube.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class VTubeStudioController:
    def __init__(self, uri: str = "ws://localhost:8001"):
        self.uri = uri
        self.ws: Optional[websockets.WebSocketClientProtocol] = None
        self.auth_token: Optional[str] = None
        self.plugin_name = "RapipiAI"
        self.plugin_developer = "YourName"
        self.config_path = Path("vtube_config.json")

        # emotion → expression mapping
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

    async def connect(self) -> bool:
        try:
            logger.debug("🔄 กำลังเชื่อมต่อกับ VTube Studio...")
            self.ws = await websockets.connect(self.uri)
            logger.info("✅ เชื่อมต่อสำเร็จ")
            return True
        except Exception as e:
            logger.error(f"❌ การเชื่อมต่อล้มเหลว: {str(e)}")
            return False

    async def _request_token(self) -> Optional[str]:
        try:
            request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": str(uuid.uuid4()),
                "messageType": "AuthenticationTokenRequest",
                "data": {
                    "pluginName": self.plugin_name,
                    "pluginDeveloper": self.plugin_developer
                }
            }
            logger.debug("🔑 ขอ Token ใหม่...")
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            data = json.loads(response)
            token = data["data"]["authenticationToken"]
            with open(self.config_path, "w") as f:
                json.dump({"auth_token": token}, f)
            logger.info("🔐 ได้รับ Token ใหม่เรียบร้อย")
            return token
        except Exception as e:
            logger.error(f"💥 ข้อผิดพลาดขณะขอ Token: {str(e)}")
            return None

    async def _validate_token(self) -> bool:
        try:
            request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": str(uuid.uuid4()),
                "messageType": "AuthenticationRequest",
                "data": {
                    "pluginName": self.plugin_name,
                    "pluginDeveloper": self.plugin_developer,
                    "authenticationToken": self.auth_token
                }
            }
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            data = json.loads(response)
            return data["data"]["authenticated"]
        except Exception as e:
            logger.error(f"💥 ข้อผิดพลาดขณะตรวจสอบ Token: {str(e)}")
            return False

    async def authenticate(self) -> bool:
        if self.config_path.exists():
            with open(self.config_path) as f:
                config = json.load(f)
                self.auth_token = config.get("auth_token")
        if not self.auth_token:
            self.auth_token = await self._request_token()
            if not self.auth_token:
                return False
        return await self._validate_token()

    async def set_expression(self, expression_file: str) -> bool:
        try:
            request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": str(uuid.uuid4()),
                "messageType": "ExpressionActivationRequest",
                "data": {
                    "expressionFile": expression_file,
                    "active": True
                }
            }
            logger.debug(f"🎭 ตั้งค่า Expression: {expression_file}")
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            logger.info(f"📤 คำตอบ: {response}")
            return True
        except Exception as e:
            logger.error(f"💥 set_expression ผิดพลาด: {str(e)}")
            return False

    async def set_emotion(self, emotion_name: str) -> bool:
        expression_file = self.emotion_to_expression.get(emotion_name)
        if not expression_file:
            logger.warning(f"⚠️ ไม่รู้จัก emotion '{emotion_name}'")
            return False
        return await self.set_expression(expression_file)

    async def close(self) -> None:
        if self.ws:
            await self.ws.close()
            logger.info("🛑 ปิดการเชื่อมต่อเรียบร้อย")

# ตัวอย่างใช้งาน
async def main():
    controller = VTubeStudioController()

    if not await controller.connect():
        return

    if not await controller.authenticate():
        logger.error("❌ ไม่สามารถตรวจสอบสิทธิ์ได้")
        return

    # 🧪 ตัวอย่าง: เปลี่ยนอารมณ์เป็น happy (จะใช้ "微笑.exp3.json")
    await controller.set_emotion("happy")

    await controller.close()

if __name__ == "__main__":
    asyncio.run(main())
