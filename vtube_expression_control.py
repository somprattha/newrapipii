import asyncio
import websockets
import json

# ฟังก์ชั่นสำหรับการขอ token
async def authenticate():
    uri = "ws://localhost:8001"
    async with websockets.connect(uri) as websocket:
        # ส่งคำขอ AuthenticationTokenRequest เพื่อขอ Token
        auth_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "authentication_request",
            "messageType": "AuthenticationTokenRequest"
        }
        await websocket.send(json.dumps(auth_request))
        response = await websocket.recv()
        print(f"Received authentication token response: {response}")
        
        # ประมวลผลการรับ Token
        response_data = json.loads(response)
        if "data" in response_data and "authenticationToken" in response_data["data"]:
            token = response_data["data"]["authenticationToken"]
            print(f"Token: {token}")
            return token
        else:
            print("Failed to retrieve authentication token.")
            return None

# ฟังก์ชั่นตั้งค่า Expression
async def set_expression(expression_name, token):
    uri = "ws://localhost:8001"
    async with websockets.connect(uri) as websocket:
        # ส่งคำขอ Authentication เพื่อให้แน่ใจว่าเชื่อมต่อแล้ว
        auth_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "authentication_request",
            "authenticationToken": token,
            "messageType": "AuthenticationRequest"
        }
        await websocket.send(json.dumps(auth_request))
        auth_response = await websocket.recv()
        print(f"Received authentication response: {auth_response}")
        
        # ตรวจสอบว่า Authentication สำเร็จหรือไม่
        auth_response_data = json.loads(auth_response)
        if not auth_response_data.get("data", {}).get("authenticated", False):
            print("Authentication failed.")
            return
        
        # ส่งคำขอเปลี่ยน Expression
        expression_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "set_expression_request",
            "messageType": "SetExpressionStateRequest",
            "data": {
                "expression": expression_name
            },
            "authenticationToken": token
        }
        await websocket.send(json.dumps(expression_request))
        
        # รับคำตอบ
        response = await websocket.recv()
        print(f"Response: {response}")

# ฟังก์ชั่นหลักที่ใช้รัน
async def vtube_studio_client():
    print("🔌 Connecting to VTube Studio...")
    token = await authenticate()
    if token:
        print("✅ Authentication Successful!")
        expression_name = "脸红"  # ชื่อของ Expression ที่คุณต้องการเปลี่ยน
        await set_expression(expression_name, token)
    else:
        print("❌ Authentication failed.")

# เรียกใช้ฟังก์ชั่นหลัก
if __name__ == "__main__":
    asyncio.run(vtube_studio_client())
