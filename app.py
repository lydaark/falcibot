from flask import Flask, render_template, request
from openai import OpenAI
import random
import os

app = Flask(__name__)

client = OpenAI()

tarot_cards = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World"
]


@app.route("/", methods=["GET", "POST"])
def index():

    yorum = None
    cards = []

    if request.method == "POST":

        question = request.form["question"]

        cards = random.sample(tarot_cards, 3)

        prompt = f"""
Kullanıcı şu soruyu sordu:
{question}

Seçilen tarot kartları:
{cards}

Bu kartlara göre mistik bir tarot falı yorumla.
Aşk, kader ve gelecek hakkında yorum yap.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        yorum = response.choices[0].message.content

    return render_template("index.html", yorum=yorum, cards=cards)


if __name__ == "__main__":
    app.run()
