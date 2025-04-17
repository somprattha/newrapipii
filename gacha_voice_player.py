
import threading
import time

def gacha_loop():
    while True:
        print("🔊 Gacha Voice: ได้ยินเสียงเค้าไหม~")
        time.sleep(600)

def trigger_gacha_voice():
    threading.Thread(target=gacha_loop, daemon=True).start()
