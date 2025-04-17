def speak_with_fallback(text, voice_style=None):
    # ลำดับ Google Chirp3 HD → Azure → Edge → Google → gTTS
    try:
        from tts_google_chirp import speak as speak_chirp3
        speak_chirp3(text, voice_style)
        return
    except Exception as e:
        print("❌ Google Chirp3 ล้มเหลว:", e)

    try:
        from tts_azure import speak as speak_azure
        speak_azure(text, voice_style)
        return
    except Exception as e:
        print("❌ Azure ล้มเหลว:", e)

    try:
        from tts_edge import speak as speak_edge
        speak_edge(text)
        return
    except Exception as e:
        print("❌ Edge ล้มเหลว:", e)

    try:
        from tts_google import speak as speak_google
        speak_google(text)
        return
    except Exception as e:
        print("❌ Google Standard ล้มเหลว:", e)

    try:
        from tts_gtts import speak as speak_gtts
        speak_gtts(text)
    except Exception as e:
        print("❌ gTTS ล้มเหลวสุดท้าย:", e)
