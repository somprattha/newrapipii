
import datetime
import shutil
import time
from threading import Thread
from lunar_checker import get_loikrathong_date

def check_loikrathong_and_switch_theme():
    today = datetime.date.today()
    loikrathong = get_loikrathong_date(today.year)

    if today == loikrathong:
        try:
            shutil.copyfile("web_overlay/themes/loikrathong/index.html", "web_overlay/index.html")
            print("🪷 เปลี่ยนธีมลอยกระทงอัตโนมัติแล้ว")

            def revert():
                time.sleep(86400)
                shutil.copyfile("web_overlay/themes/default/index.html", "web_overlay/index.html")
                print("🔁 กลับเป็นธีมปกติแล้ว")
            Thread(target=revert).start()
        except Exception as e:
            print("⚠️ เปลี่ยนธีมลอยกระทงไม่สำเร็จ:", e)
