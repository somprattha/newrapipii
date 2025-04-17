import json
import os

FAN_WALLET_FILE = "fan_wallet.json"

def load_fan_wallet():
    if not os.path.exists(FAN_WALLET_FILE):
        return {}
    with open(FAN_WALLET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_fan_wallet(wallet):
    with open(FAN_WALLET_FILE, "w", encoding="utf-8") as f:
        json.dump(wallet, f, indent=2, ensure_ascii=False)

def get_vip_level_by_coin(coin):
    if coin >= 10000:
        return "👑"
    elif coin >= 5000:
        return "💖"
    elif coin >= 2000:
        return "🌟"
    else:
        return "⭐"

def get_user_vip(username):
    wallet = load_fan_wallet()
    coin = wallet.get(username, 0)
    return get_vip_level_by_coin(coin)

def add_coin(username, amount=10):
    wallet = load_fan_wallet()
    wallet[username] = wallet.get(username, 0) + amount
    save_fan_wallet(wallet)