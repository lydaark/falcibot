from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/fal", methods=["POST"])
def fal():
    data = request.get_json()

    if not data or "soru" not in data:
        return jsonify({"cevap": "Soru alınamadı."})

    soru = data["soru"]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen cool ve mistik bir falcısın. Kısa ve etkileyici cevap ver."},
                {"role": "user", "content": soru}
            ]
        )

        return jsonify({
            "cevap": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            "cevap": "Sunucu hatası: " + str(e)
        })

if __name__ == "__main__":
    app.run()
