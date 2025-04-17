def identify_speaker(audio_chunk):
    # จำลองการแยกว่าใครพูด (เช่น โดยใช้ embedding เสียง)
    return "owner" if "owner_signature" in audio_chunk else "viewer"