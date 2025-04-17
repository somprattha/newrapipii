async def authenticate(self):
    """กระบวนการขอ Token และตรวจสอบสิทธิ์"""
    try:
        # ขอ Token ใหม่
        token_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "get-token-001",
            "messageType": "AuthenticationTokenRequest",
            "data": {
                "pluginName": self.plugin_name,
                "pluginDeveloper": self.plugin_developer
            }
        }
        logger.info("🔑 ส่งคำขอ Token...")
        await self.ws.send(json.dumps(token_request))
        token_response = await self.ws.recv()
        logger.info(f"📥 คำตอบ Token: {token_response}")  # แสดงข้อมูลตอบกลับดิบ
        
        token_data = json.loads(token_response)
        self.auth_token = token_data["data"]["authenticationToken"]

        # ใช้ Token เพื่อตรวจสอบสิทธิ์
        auth_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "auth-001",
            "messageType": "AuthenticationRequest",
            "data": {
                "pluginName": self.plugin_name,
                "pluginDeveloper": self.plugin_developer,
                "authenticationToken": self.auth_token
            }
        }
        logger.info("🔒 ส่งคำขอตรวจสอบสิทธิ์...")
        await self.ws.send(json.dumps(auth_request))
        auth_response = await self.ws.recv()
        logger.info(f"📥 คำตอบตรวจสอบสิทธิ์: {auth_response}")  # แสดงข้อมูลตอบกลับดิบ

    except Exception as e:
        logger.error(f"💥 ข้อผิดพลาดในการตรวจสอบสิทธิ์: {str(e)}")
        raise  # โยนข้อผิดพลาดต่อเพื่อหยุดการทำงาน