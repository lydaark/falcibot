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
                {"role": "system", "content": "Sen gizemli, karizmatik ve biraz tehlikeli bir falcısın. Kısa ve etkileyici cevap ver."},
                {"role": "user", "content": f"Kullanıcının sorusu: {soru}. Ona gizemli bir fal bak."}
            ]
        )

        return jsonify({
            "cevap": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            "cevap": f"HATA: {str(e)}"
        })

if __name__ == "__main__":
    app.run()
