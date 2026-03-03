from flask import Flask, request, jsonify
from openai import OpenAI
client = OpenAI()
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
    from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/fal", methods=["POST"])
def fal():
    data = request.json
    soru = data.get("soru")

  from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__, static_folder=".")

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/fal", methods=["POST"])
def fal():
    data = request.json
    soru = data.get("soru")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen mistik bir falcısın. Kullanıcının sorusuna etkileyici, kısa ve gizemli cevap ver."},
            {"role": "user", "content": soru}
        ]
    )

    cevap = response["choices"][0]["message"]["content"]

    return jsonify({"cevap": cevap})

if __name__ == "__main__":
    app.run()

    return jsonify({
        "cevap": response.choices[0].message.content
    })


if __name__ == "__main__":
    app.run()
