
def update_emotion(message):
    if "น่ารัก" in message:
        print("😊 Emotion: Happy")
        return "happy"
    elif "คิดถึง" in message:
        print("🥺 Emotion: Sad")
        return "sad"
    else:
        print("😐 Emotion: Neutral")
        return "neutral"
