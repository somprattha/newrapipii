# websocket_client.py

import websocket
import json

# การเชื่อมต่อ VTube Studio
def connect_vtube():
    try:
        ws = websocket.create_connection("ws://127.0.0.1:8001")  # URL นี้อาจจะต้องเปลี่ยนเป็น IP ของ VTube Studio
        print("Connected to VTube Studio WebSocket")
        return ws
    except Exception as e:
        print(f"Failed to connect to VTube Studio: {e}")
        return None

# ส่งคำสั่งให้ VTube Studio เปลี่ยนอารมณ์
def set_emotion_to_vtube(ws, emotion):
    if ws is not None:
        emotion_data = {
            "event_type": "set_emotion",
            "emotion": emotion
        }
        ws.send(json.dumps(emotion_data))
        print(f"Sent emotion: {emotion}")
    else:
        print("Not connected to VTube Studio")
