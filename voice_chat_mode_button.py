from tkinter import *
import threading
from mic_command_trigger import start_voice_command_listener, stop_voice_command_listener

def toggle_voice_mode():
    global voice_active
    if not voice_active:
        voice_active = True
        voice_btn.config(text="🛑 หยุดฟังเสียง", bg="#ffaaaa")
        threading.Thread(target=start_voice_command_listener).start()
    else:
        voice_active = False
        voice_btn.config(text="🎤 เริ่มสนทนาด้วยเสียง", bg="#ccffcc")
        stop_voice_command_listener()

root = Tk()
root.title("โหมดสนทนา Rapipii")
voice_active = False

voice_btn = Button(root, text="🎤 เริ่มสนทนาด้วยเสียง", command=toggle_voice_mode, bg="#ccffcc", width=40)
voice_btn.pack(pady=20)

root.mainloop()