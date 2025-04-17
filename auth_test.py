import websockets
import asyncio
import json
import logging

logging.basicConfig(level=logging.DEBUG)

async def send_auth_request():
    uri = "ws://localhost:8001"
    try:
        async with websockets.connect(uri) as ws:
            # ขอ Token
            request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "Auth_1",
                "messageType": "AuthenticationTokenRequest",
                "data": {
                    "pluginName": "RapipiAI",
                    "pluginDeveloper": "YourName"
                }
            }
            await ws.send(json.dumps(request))
            response = await ws.recv()
            print("ตอบกลับ:", json.loads(response))
            
    except Exception as e:
        logging.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")

asyncio.run(send_auth_request())