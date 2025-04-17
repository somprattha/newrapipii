# overlay_vip_streamer.py — Overlay แบบ VTuber มืออาชีพ
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import os

def show_vip_overlay_streamer(username, message, vip_level="💖", duration=6):
    emoji = {
        "⭐": "✨", "🌟": "🌟", "💖": "💖", "👑": "👑"
    }.get(vip_level, "✨")

    # เตรียมหน้าต่าง
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="black")
    root.geometry("600x150+100+100")
    root.wm_attributes("-alpha", 0.0)  # เริ่มโปร่งใส

    # โหลด gif ภาพประกอบ (ใส่ไว้ในโฟลเดอร์เดียวกัน)
    gif_path = "kawaii_heart.gif"
    gif_image = None
    if os.path.exists(gif_path):
        gif_raw = Image.open(gif_path)
        gif_image = ImageTk.PhotoImage(gif_raw.resize((100, 100)))

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    if gif_image:
        canvas.create_image(50, 75, image=gif_image)

    text_id = canvas.create_text(
        200, 75, anchor="w",
        text=f"{emoji} ขอบคุณ {username}! {message} {emoji}",
        font=("Leelawadee UI", 24, "bold"),
        fill="white"
    )

    def fade_in():
        for i in range(20):
            root.wm_attributes("-alpha", i / 20)
            time.sleep(0.03)

    def fade_out():
        for i in reversed(range(20)):
            root.wm_attributes("-alpha", i / 20)
            time.sleep(0.03)
        root.destroy()

    def run():
        fade_in()
        time.sleep(duration)
        fade_out()

    threading.Thread(target=run).start()
    root.mainloop()