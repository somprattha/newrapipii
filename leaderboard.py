# leaderboard.py — จัดอันดับแฟนคลับตาม RPP Coin
import json

def get_top_fans(file="fan_wallet.json", top_n=5):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        sorted_users = sorted(data.items(), key=lambda x: x[1].get("rpp_coin", 0), reverse=True)
        return sorted_users[:top_n]
    except:
        return []