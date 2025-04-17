from vtube_controller import VTubeStudioController

class RapipiiAI:
    def __init__(self):
        self.vtube_controller = VTubeStudioController()
        self.current_emotion = "neutral"
        self.last_sent_emotion = None

    async def start(self):
        await self.vtube_controller.connect()

    async def stop(self):
        await self.vtube_controller.close()

    async def on_emotion_change(self, new_emotion):
        self.current_emotion = new_emotion

        # ส่ง expression เฉพาะถ้าเปลี่ยนจริงๆ
        if new_emotion != self.last_sent_emotion:
            await self.vtube_controller.set_expression(new_emotion)
            self.last_sent_emotion = new_emotion
