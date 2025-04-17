def apply_personality(response, mode="friendly"):
    if mode == "friendly":
        return f"~ 😊 {response}"
    elif mode == "cool":
        return f"😎 Yo! {response}"
    elif mode == "smart":
        return f"📘 {response} (analyzed response)"
    return response