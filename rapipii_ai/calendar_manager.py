def get_today_theme(): return '🎂 Happy Birthday แฟนคลับ!'

from datetime import datetime

def get_special_day_voice(name=None):
    today = datetime.now().strftime("%m-%d")
    if today == "01-15" and name:
        return f"สุขสันต์วันเกิดนะคะ {name}~ วันนี้ของคุณพิเศษที่สุดเลย~ 🎂"
    elif today == "08-12":
        return "วันนี้วันแม่แห่งชาติ ราปิปี้ขอส่งความรักให้คุณแม่ของทุกคนเลยน้า~ 💐"
    elif today == "12-25":
        return "เมอร์รี่คริสต์มาส~ ขอให้มีแต่ความสุขเหมือนหิมะโปรยปรายเลยน้า~ 🎄"
    elif today == "04-13":
        return "สุขสันต์วันสงกรานต์~ ขอให้เย็นชื่นหัวใจเหมือนน้ำสาดเลยนะคะ 💦"
    elif today == "01-01":
        return "สวัสดีปีใหม่~ ขอให้ปีนี้เต็มไปด้วยรอยยิ้มและความอบอุ่นนะคะ 🎆"
    else:
        return None
# calendar_manager.py (append)
from datetime import datetime

def get_special_day_voice():
    today = datetime.now()
    if today.month == 2 and today.day == 14:
        return "สุขสันต์วันวาเลนไทน์น้า~ ราปิปี้รักทุกคนเลย~ 💖"
    return ""

# 🎉 ปีใหม่ + ส่งท้ายปี
def get_special_day_voice():
    from datetime import datetime
    today = datetime.now()
    if today.month == 1 and today.day == 1:
        return "สุขสันต์วันปีใหม่ค่า~ ขอให้ปีนี้เต็มไปด้วยรอยยิ้มและความสุขนะคะ~ 🎉"
    elif today.month == 12 and today.day == 31:
        return "วันนี้วันส่งท้ายปีเก่าแล้ว~ ขอบคุณที่อยู่กับราปิปี้ตลอดปีนะคะ~ 💖"
    return ""

# 🕊️ วันพ่อแห่งชาติ
def get_special_day_voice():
    from datetime import datetime
    today = datetime.now()
    if today.month == 12 and today.day == 5:
        return "สุขสันต์วันพ่อค่ะ~ ขอให้คุณพ่อสุขภาพแข็งแรง และมีความสุขในทุกวันนะคะ~ 🕊️"
    return ""