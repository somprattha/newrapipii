
import os
import random
from datetime import datetime, timedelta
import pytz

from tts_modules.google_chirp3 import generate_with_chirp3
from tts_modules.azure_tts import generate_with_azure
from tts_modules.edge_tts import generate_with_edge
from tts_modules.google_standard import generate_with_google_standard
from tts_modules.gtts_fallback import generate_with_gtts

THAI_TZ = pytz.timezone('Asia/Bangkok')

class TTSManager:
    def __init__(self):
        self.quotas = {
            'chirp3': {'limit': 1_000_000, 'used': 0},
            'azure': {'limit': 500_000, 'used': 0},
            'google_std': {'limit': 4_000_000, 'used': 0},
            'edge': {'limit': float('inf'), 'used': 0},
            'gtts': {'limit': float('inf'), 'used': 0},
        }
        self.last_reset = self.get_bangkok_day_start()

    def get_bangkok_day_start(self):
        now = datetime.now(THAI_TZ)
        return now.replace(hour=7, minute=0, second=0, microsecond=0)

    def check_and_reset_quota(self):
        now = datetime.now(THAI_TZ)
        if now >= self.last_reset + timedelta(days=1):
            for provider in self.quotas:
                self.quotas[provider]['used'] = 0
            self.last_reset = self.get_bangkok_day_start()

    def count_words(self, text):
        return len(text.split())

    def select_provider(self):
        for provider in ['chirp3', 'azure', 'edge', 'google_std', 'gtts']:
            quota = self.quotas[provider]
            if quota['used'] < quota['limit'] * 0.99:
                return provider
        return 'gtts'

    def speak(self, text, out_path='output.wav'):
        self.check_and_reset_quota()

        provider = self.select_provider()
        word_count = self.count_words(text)
        self.quotas[provider]['used'] += word_count

        try:
            if provider == 'chirp3':
                generate_with_chirp3(text, out_path)
            elif provider == 'azure':
                generate_with_azure(text, out_path)
            elif provider == 'edge':
                generate_with_edge(text, out_path)
            elif provider == 'google_std':
                generate_with_google_standard(text, out_path)
            else:
                generate_with_gtts(text, out_path)

            # ส่งเสียงไป VB Audio Virtual Cable
            os.system(f"ffplay -nodisp -autoexit -loglevel quiet {out_path}")

        except Exception as e:
            print(f"TTS error [{provider}]: {e}")
