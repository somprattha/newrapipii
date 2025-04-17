import time
import google.auth
from googleapiclient.discovery import build
from threading import Thread

from utils.emotion_analyzer import analyze_emotion
from utils.tts_controller import speak_text
from utils.persona_switcher import switch_persona
from websocket_client import set_emotion_to_vtube  # นำเข้า WebSocket client

# === ตั้งค่าหลัก ===
YOUTUBE_API_KEYS = [
    "AIzaYourKey1",
    "AIzaYourKey2",
    "AIzaYourKey3",  # ใส่หลายอันเพื่อ auto fallback
]
CHANNEL_ID = "UCHi24aU7rjqYiOlTB5W5q9w"

# === ระบบ auto หมุน API Key ===
api_index = 0

def get_youtube_service():
    global api_index
    key = YOUTUBE_API_KEYS[api_index % len(YOUTUBE_API_KEYS)]
    api_index += 1
    return build("youtube", "v3", developerKey=key)

# === ดึง chat id จาก live broadcast ===
def get_live_chat_id(youtube):
    req = youtube.liveBroadcasts().list(
        part="snippet",
        broadcastStatus="active",
        broadcastType="all"
    )
    res = req.execute()
    if not res["items"]:
        return None
    return res["items"][0]["snippet"]["liveChatId"]

# === ตัวหลัก: ฟังแชทแบบเรียลไทม์ ===
def listen_chat():
    def run():
        youtube = get_youtube_service()
        chat_id = get_live_chat_id(youtube)
        if not chat_id:
            print("[YouTubeChat] ❌ ไม่พบ Live หรือยังไม่ได้กดเริ่มถ่ายทอด")
            return

        print(f"[YouTubeChat] ✅ เชื่อมต่อ Live Chat แล้ว (ID: {chat_id})")
        nextPageToken = None

        while True:
            try:
                res = youtube.liveChatMessages().list(
                    liveChatId=chat_id,
                    part="snippet,authorDetails",
                    maxResults=200,
                    pageToken=nextPageToken
                ).execute()

                for item in res.get("items", []):
                    msg = item["snippet"]["displayMessage"]
                    author = item["authorDetails"]["displayName"]
                    is_member = item["authorDetails"].get("isChatSponsor", False)
                    superchat = item["snippet"].get("superChatDetails")

                    print(f"[Chat] {author}: {msg}")

                    # วิเคราะห์อารมณ์ + เปลี่ยน Persona
                    mood = analyze_emotion(msg)
                    switch_persona(mood)

                    # ตอบกลับด้วยเสียง
                    if superchat:
                        amount = superchat["amountDisplayString"]
                        speak_text(f"ขอบคุณสำหรับ SuperChat {amount} นะ {author}~! รักที่สุดเลย 💖")
                    elif is_member:
                        speak_text(f"ขอบคุณที่เป็นสมาชิกนะ {author}~! อยู่กับเรานานๆนะ~")
                    else:
                        speak_text(f"{author} พิมพ์ว่า {msg}")

                nextPageToken = res.get("nextPageToken")
                time.sleep(4.5)  # ป้องกันโดนจำกัด rate
            except Exception as e:
                print("[YouTubeChat] ⚠️ พบข้อผิดพลาด:", e)
                time.sleep(10)

    Thread(target=run, daemon=True).start()

# ฟังก์ชันที่ใช้สำหรับการส่งคำสั่งอารมณ์ไป VTube Studio
def on_chat_message_received(message):
    # ส่งคำสั่งไปยัง VTube Studio เพื่อเปลี่ยนอารมณ์
    ws = connect_vtube()  # เชื่อมต่อ WebSocket
    emotion = analyze_emotion(message)  # วิเคราะห์อารมณ์
    set_emotion_to_vtube(ws, emotion)  # ส่งคำสั่งไป VTube Studio

# ฟังก์ชันที่จะถูกเรียกเมื่อข้อความแชทใหม่เข้ามา
def update_expression_based_on_chat(message):
    on_chat_message_received(message)
