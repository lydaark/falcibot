from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Falci Bot çalışıyor 🔮"

@app.route("/fal", methods=["POST"])
def fal():
    data = request.json
    soru = data.get("soru")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen mistik bir falcısın."},
            {"role": "user", "content": soru}
        ]
    )

    cevap = response.choices[0].message.content
    return jsonify({"cevap": cevap})
