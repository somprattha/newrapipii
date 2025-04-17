
import threading
import time

def self_talk():
    while True:
        print("💬 AI: ดูแลตัวเองด้วยน้า~")
        time.sleep(120)

def start_self_talk():
    threading.Thread(target=self_talk, daemon=True).start()
