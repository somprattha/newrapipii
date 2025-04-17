from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__, template_folder="templates")

QUOTA_FILE = "tts_quota.json"
QUOTAS = {
    "azure_tts": 500_000,
    "google_chirp3_hd_tts": 1_000_000,
    "edge_tts": float('inf'),
    "google_standard_tts": 4_000_000,
    "gtts_fallback": float('inf')
}

@app.route("/api/tts/quota")
def get_tts_quota():
    try:
        if not os.path.exists(QUOTA_FILE):
            quota_data = {k: 0 for k in QUOTAS.keys()}
        else:
            with open(QUOTA_FILE, 'r') as f:
                quota_data = json.load(f)

        result = {}
        for k in QUOTAS:
            used = quota_data.get(k, 0)
            total = QUOTAS[k] if QUOTAS[k] != float('inf') else None
            percent = round((used / total) * 100, 2) if total else None
            result[k] = {
                "used": used,
                "total": total,
                "percent": percent
            }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/tts-quota")
def show_quota_page():
    return render_template("tts_quota_dashboard.html")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
