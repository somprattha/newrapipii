
import threading
import subprocess

modules = [
    "hydration_reminder_runner.py",
    "idle_angry_runner.py",
    "random_talker_runner.py",
    "mic_command_trigger.py",  # ฟังเสียงจากไมค์แล้วตอบ
    "chat_listener.py"         # ฟังข้อความจากแชทแล้วตอบ
]

def run_module(file):
    subprocess.Popen(["python", file])

if __name__ == "__main__":
    print("🚀 [Rapipii Ultimate Launcher] เริ่มทุกระบบพร้อมกัน...")
    for m in modules:
        threading.Thread(target=run_module, args=(m,)).start()
