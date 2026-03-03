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

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
               {"role": "system", "content": "Sen gizemli, karizmatik ve biraz tehlikeli bir falcısın. İnsanların duygularını hissediyorsun. Cevapların kısa, çarpıcı ve merak uyandırıcı olmalı. Bazen net konuşma, bazen üstü kapalı söyle. Kullanıcıyı düşündür ve biraz bağımlı yap."}
                {"role": "user", "content": soru}
            ]
        )

        cevap = response.choices[0].message.content

        return jsonify({"cevap": cevap})

    except Exception as e:
        return jsonify({"cevap": f"HATA: {str(e)}"})

if __name__ == "__main__":
    app.run()
