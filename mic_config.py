# mic_config.py

import sounddevice as sd

# 🛠 เปลี่ยนเป็น 44 หรือ 17 แล้วแต่ไมค์ที่พี่ต้องการ
MICROPHONE_NAME = 44  # ใช้ WASAPI ซึ่งแม่นยำกว่าปกติ

# ถ้าต้องการเช็กอุปกรณ์ทั้งหมด (รันครั้งเดียว)
if __name__ == "__main__":
    for i, dev in enumerate(sd.query_devices()):
        print(f"[{i}] {dev['name']}")
