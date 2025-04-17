# emotion_trigger_hook.py
from calendar_manager import get_special_day_voice
import random

def emotion_from_gacha(rarity):
    if rarity == "SSR":
        return "moe.vtsexpression"
    elif rarity == "SR":
        return "blush.vtsexpression"
    elif rarity == "R":
        return "cry.vtsexpression"
    return "neutral.vtsexpression"

def emotion_from_calendar():
    message = get_special_day_voice()
    if "สุขสันต์วันเกิด" in message:
        return "blush.vtsexpression"
    elif "สงกรานต์" in message:
        return "moe.vtsexpression"
    elif "คริสต์มาส" in message:
        return "blush.vtsexpression"
    return "neutral.vtsexpression"