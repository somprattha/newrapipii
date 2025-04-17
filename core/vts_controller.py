import asyncio
import websockets
import json

class VTubeStudioConnector:
    def __init__(self, uri="ws://localhost:8001"):
        self.uri = uri
        self.websocket = None

    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.uri)
            print("✅ เชื่อมต่อกับ VTube Studio สำเร็จ")
        except Exception as e:
            print(f"❌ ไม่สามารถเชื่อมต่อ VTube Studio: {e}")

    async def set_parameter(self, param_id, value):
        if self.websocket:
            message = {
                "apiName": "VTubeStudioPublicAPI",
                "messageType": "InjectParameterDataRequest",
                "data": {
                    "parameterValues": [
                        {"id": param_id, "value": value}
                    ]
                }
            }
            try:
                await self.websocket.send(json.dumps(message))
            except Exception as e:
                print(f"❌ ส่งข้อมูล VTS ล้มเหลว: {e}")

    async def speak(self):
        # จำลองการขยับปาก
        await self.set_parameter("ParamMouthOpen", 1.0)
        await asyncio.sleep(0.2)
        await self.set_parameter("ParamMouthOpen", 0.0)

# ใช้แบบ standalone ทดสอบได้
if __name__ == "__main__":
    async def test():
        vts = VTubeStudioConnector()
        await vts.connect()
        await vts.speak()
    asyncio.run(test())