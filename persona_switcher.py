
def switch_persona(emotion, message):
    if "vip" in message:
        print("🔄 Persona: VIP Mode")
    elif emotion == "happy":
        print("🔄 Persona: Playful Mode")
    elif emotion == "sad":
        print("🔄 Persona: Comfort Mode")
    else:
        print("🔄 Persona: Default")
