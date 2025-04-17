# fan_manager.py
import json

FAN_MEMORY_FILE = "fan_memory.json"  # ตั้งไฟล์สำหรับจัดเก็บข้อมูลแฟนคลับ

def load_fan_memory():
    try:
        with open(FAN_MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # ถ้าไม่มีไฟล์คืนค่ากลับเป็นดิกชันนารีว่าง

def save_fan_memory(fan_memory):
    with open(FAN_MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(fan_memory, f, indent=2, ensure_ascii=False)

def fan_memory_manager():
    fan_memory = load_fan_memory()
    
    # เพิ่มข้อมูลแฟนคลับที่นี่ (ตัวอย่าง)
    # เช่น เพิ่มชื่อแฟนคลับใหม่:
    fan_memory["fan_name"] = "ตัวอย่างแฟนคลับ"
    fan_memory["fan_id"] = 1

    # แสดงข้อมูลแฟนคลับ
    print(f"📜 ข้อมูลแฟนคลับ: {fan_memory}")

    # บันทึกข้อมูลใหม่
    save_fan_memory(fan_memory)
