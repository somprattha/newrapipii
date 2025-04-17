vip_users_list = [
    "UCxxxxx1",
    "UCxxxxx2",
    "UCHi24aU7rjqYiOlTB5W5q9w"
]

def is_vip_user(user_id):
    return user_id in vip_users_list

def assign_vip_voice(user_id):
    if user_id == "UCHi24aU7rjqYiOlTB5W5q9w":
        return "voice_fan_shy_adorable"
    elif is_vip_user(user_id):
        return "voice_warm_caring"
    else:
        return "voice_normal"

def add_vip_user(user_id):
    if user_id not in vip_users_list:
        vip_users_list.append(user_id)

def remove_vip_user(user_id):
    if user_id in vip_users_list:
        vip_users_list.remove(user_id)