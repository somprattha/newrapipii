import json

def show_fan_stats():
    try:
        with open("fan_memory.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print("📊 สถิติแฟนคลับย้อนหลัง:")
        for fan, info in data.items():
            print(f"👤 {fan} → {info['count']} ข้อความล่าสุด: {info['last_message']}")
    except:
        print("ยังไม่มีข้อมูลแฟนเลยนะ~ 😢")