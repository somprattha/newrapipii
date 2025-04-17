# emoji_name_matcher.py
emoji_name_map = {
    "🦊": "FoxyBoy",
    "🐱": "น้องเหมียว",
    "🐰": "โมเอะบันนี่",
    "🐻": "นุ่มฟูแบร์"
}

def get_name_by_emoji(emoji):
    return emoji_name_map.get(emoji, "ไม่รู้จักนะ~")