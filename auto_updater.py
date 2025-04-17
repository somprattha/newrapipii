def check_for_updates(current_version):
    # จำลองตรวจเวอร์ชันใหม่
    latest_version = "1.0.1"
    if current_version != latest_version:
        print(f"New version {latest_version} available!")
        return True
    return False