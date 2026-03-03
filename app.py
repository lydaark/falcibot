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
    try:
        data = request.json
        soru = data.get("soru")

        if not soru:
            return jsonify({"cevap": "Bir soru yazmalısın..."}), 400

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen mistik, cool ve gizemli bir falcısın. Kısa ve etkileyici cevaplar ver."},
                {"role": "user", "content": soru}
            ]
        )

        cevap = response.choices[0].message.content

        return jsonify({"cevap": cevap})

    except Exception as e:
        print("HATA:", str(e))
        return jsonify({"cevap": "Fal kapalı... enerjiler karışık 🔮"}), 500


if __name__ == "__main__":
    app.run()
