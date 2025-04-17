import re

def remove_emojis(text: str) -> str:
    """
    ลบอิโมจิออกจากข้อความ
    """
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F"
        "\U0001FA70-\U0001FAFF\U00002702-\U000027B0\U000024C2-\U0001F251]+", flags=re.UNICODE)
    return emoji_pattern.sub('', text)

def remove_symbols_and_emotions(text: str) -> str:
    """
    ลบสัญลักษณ์หรือข้อความที่เป็นอารมณ์ เช่น :) , :( , :P
    """
    # ลบอารมณ์อย่าง :) , :( , :P เป็นต้น
    text = re.sub(r'[:;=][\)\(\/\\\|]?', '', text)
    # ลบสัญลักษณ์ที่ไม่จำเป็น เช่น * # & @ !
    text = re.sub(r'[\*\#\&\@\!]', '', text)
    return text

def clean_text_for_tts(text: str) -> str:
    """
    ฟังก์ชันหลักในการกรองข้อความที่ไม่จำเป็นออกก่อนส่งให้ TTS
    """
    text = remove_emojis(text)
    text = remove_symbols_and_emotions(text)
    return text

# ฟังก์ชันทดสอบ
def test_cleaning():
    sample_text = "Hello there! 😊 How are you? 😄 #TTS 😜"
    cleaned_text = clean_text_for_tts(sample_text)
    
    print("Before Cleaning:", sample_text)
    print("After Cleaning:", cleaned_text)

# ทดสอบการกรอง
test_cleaning()
