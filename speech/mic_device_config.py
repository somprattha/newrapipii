
import sounddevice as sd

def list_microphones():
    devices = sd.query_devices()
    mics = [d['name'] for d in devices if d['max_input_channels'] > 0]
    return mics

def get_default_microphone():
    try:
        default = sd.query_devices(kind='input')
        return default['name']
    except Exception as e:
        print(f"[MIC] ❌ ไม่พบไมโครโฟนเริ่มต้น: {e}")
        return None
