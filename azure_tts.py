import os
import requests

def azure_tts(text, voice="th-TH-PremwadeeNeural"):
    endpoint = os.getenv("AZURE_TTS_ENDPOINT", "https://southeastasia.tts.speech.microsoft.com/cognitiveservices/v1")
    key = os.getenv("AZURE_TTS_KEY")
    if not key:
        raise Exception("Azure TTS key not found in environment variables")

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3"
    }

    ssml = "<speak version='1.0' xml:lang='th-TH'><voice name='" + voice + "'>" + text + "</voice></speak>"

    response = requests.post(endpoint, headers=headers, data=ssml.encode('utf-8'))
    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        os.system("start output.mp3")
    else:
        raise Exception(f"Azure TTS failed: {response.status_code} {response.text}")