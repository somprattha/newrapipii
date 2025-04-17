
import shutil, time, datetime
from threading import Thread
import json

def switch_overlay_for_birthday(username="ฉ่ำอุรา"):
    today = datetime.datetime.now().strftime("%m-%d")

    # โหลดวันเกิดทั้งหมด
    try:
        with open("fan_birthday.json", "r", encoding="utf-8") as f:
            fan_bdays = json.load(f)
    except Exception as e:
        print("ไม่พบ fan_birthday.json:", e)
        return

    if username in fan_bdays and fan_bdays[username] == today:
        try:
            shutil.copyfile("web_overlay/themes/birthday/index.html", "web_overlay/index.html")
            print("🎂 แสดงธีมวันเกิดให้กับ", username)

            # ✅ รอ 1 ชั่วโมงแล้วเปลี่ยนกลับ
            def revert_theme():
                time.sleep(3600)  # 1 ชั่วโมง
                shutil.copyfile("web_overlay/themes/default/index.html", "web_overlay/index.html")
                print("🔁 กลับเป็นธีมปกติแล้ว")

            Thread(target=revert_theme).start()
        except Exception as e:
            print("เกิดข้อผิดพลาดในการสลับธีม:", e)
