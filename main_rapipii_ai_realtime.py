import time
import json
import pygame
import asyncio
from core.vts_controller import VTubeStudioConnector
from fan_manager import fan_memory_manager

# กำหนดการเชื่อมต่อกับ VTube Studio
vts = VTubeStudioConnector()

# โหลดข้อมูลการตั้งค่าของ Persona
CONFIG_PATH = "config/persona_config.json"

def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"mode": "talkative", "last_auto_speak_time": 0}

def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)

def should_talk(interval_sec=120):
    cfg = load_config()
    now = time.time()
    if now - cfg["last_auto_speak_time"] >= interval_sec:
        cfg["last_auto_speak_time"] = now
        save_config(cfg)
        return True
    return False

def set_mode(new_mode):
    cfg = load_config()
    cfg["mode"] = new_mode
    save_config(cfg)
    print(f"[🧠] เปลี่ยนโหมดพูด: {new_mode}")

def get_mode():
    return load_config().get("mode", "talkative")

# ฟังก์ชันหลัก
async def main():
    # เรียกใช้งาน fan_memory_manager
    fan_memory_manager()
    
    # ทดสอบการพูด
    if should_talk():
        print("ถึงเวลาที่ AI จะพูด!")
        set_mode("talkative")
        # คุณสามารถเพิ่มการพูดหรือส่งข้อมูลไป VTube Studio ที่นี่

# เรียกใช้งานฟังก์ชันหลัก
if __name__ == "__main__":
    asyncio.run(main())
