from core.owner_identity import is_owner

def generate_reply(username, message):
    if is_owner(username):
        return "คุณฉ่ำอุรา~ 💗 เจ้าของของราปิปี้กลับมาแล้ววว~"
    elif "คิดถึง" in message:
        return f"คุณ {username}~ คิดถึงเหมือนกันค่ะ 🐰"
    elif "เศร้า" in message:
        return f"คุณ {username}~ อย่าเพิ่งเศร้าน้า ราปิปี้อยู่ตรงนี้เสมอ 💞"
    else:
        return f"ขอบคุณที่แวะมานะคะคุณ {username}~ 🌸"
