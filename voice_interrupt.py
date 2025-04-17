import sounddevice as sd
import queue
import threading

# 🔧 ตั้งชื่อไมโครโฟนที่ต้องการใช้
def get_mic_index_by_name(name_part):
    devices = sd.query_devices()
    for idx, dev in enumerate(devices):
        if name_part.lower() in dev['name'].lower():
            print(f"🔊 ใช้ไมค์: {dev['name']} (index {idx})")
            return idx
    print("⚠️ ไม่พบไมค์ที่ต้องการ ใช้ default แทน")
    return None

mic_index = get_mic_index_by_name("AMD Streaming Audio Device")
if mic_index is not None:
    sd.default.device = mic_index

# 🎧 เริ่มฟังเสียงจากไมค์ (ฟังก์ชันนี้จะรันใน thread)
def start_listening():
    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(f"⚠️ Mic Error: {status}")
        q.put(indata.copy())

    def listen_loop():
        with sd.InputStream(samplerate=16000, channels=1, callback=callback):
            while True:
                data = q.get()
                # 🔇 ตรงนี้สามารถเพิ่ม logic วิเคราะห์เสียงได้
                pass

    thread = threading.Thread(target=listen_loop, daemon=True)
    thread.start()
    print("🎤 เริ่มฟังเสียงจากไมค์แล้ว...")

# เรียกใช้เมื่อรัน
if __name__ == "__main__":
    start_listening()