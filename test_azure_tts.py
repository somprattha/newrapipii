import requests

# 🔧 ใส่คีย์ของคุณตรงนี้
AZURE_KEY = "7eyk9Mmk8BZDgIQGbRX6PGzpIORbo5UArqofVwdnICgttRr4E0tbJQQJ99BDACqBBLyXJ3w3AAAYACOGALqy"
AZURE_REGION = "southeastasia"
ENDPOINT = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"

ssml = """
<speak version='1.0' xml:lang='th-TH'>
    <voice xml:lang='th-TH' xml:gender='Female' name='th-TH-PremwadeeNeural'>
        สวัสดีค่ะ ทดสอบเสียงจาก Azure TTS โดยราปิปี้นะคะ
    </voice>
</speak>
"""

headers = {
    "Ocp-Apim-Subscription-Key": AZURE_KEY,
    "Content-Type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3"
}

print("🔄 กำลังทดสอบ Azure TTS...")

res = requests.post(ENDPOINT, headers=headers, data=ssml.encode("utf-8"))

if res.status_code == 200:
    with open("azure_test.mp3", "wb") as f:
        f.write(res.content)
    print("✅ สำเร็จ! บันทึกเสียงไว้ที่ azure_test.mp3 แล้ว")
else:
    print("❌ ล้มเหลว:", res.status_code)
    print(res.text[:500])