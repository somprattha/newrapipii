# mini_game.py — ระบบมินิเกมง่าย ๆ ผ่านแชทคำสั่ง
import random

def play_guess_number(user_input):
    try:
        guess = int(user_input.strip().split()[-1])
        correct = random.randint(1, 5)
        if guess == correct:
            return f"🎉 ทายถูก! เลขคือ {correct} ได้เหรียญเพิ่มนะ!"
        else:
            return f"😅 เสียใจจัง~ เลขคือ {correct} ไว้ลองใหม่~"
    except:
        return "❗ โปรดพิมพ์: !ทายเลข [1-5]"

def play_rps(choice):
    ai = random.choice(["ค้อน", "กรรไกร", "กระดาษ"])
    result = "เสมอ~" if ai == choice else "ชนะ!" if (ai, choice) in [("กรรไกร", "กระดาษ"), ("กระดาษ", "ค้อน"), ("ค้อน", "กรรไกร")] else "แพ้~"
    return f"🖐️ ราปิปี้ออก {ai} — คุณ {result}"