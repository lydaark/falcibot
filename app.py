from flask import Flask, render_template, request
from openai import OpenAI
import os
import random

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tarot_cards = [
"The Fool","The Magician","The High Priestess","The Empress",
"The Emperor","The Lovers","The Chariot","Strength","The Hermit",
"Wheel of Fortune","Justice","The Hanged Man","Death",
"Temperance","The Devil","The Tower","The Star","The Moon",
"The Sun","Judgement","The World"
]

@app.route("/", methods=["GET","POST"])
def index():

    yorum=None
    cards=[]

    if request.method=="POST":

        question=request.form["question"]

        cards=request.form.get("cards")

        if cards:
            cards=cards.split(",")
        else:
            cards=random.sample(tarot_cards,3)

        prompt=f"""
Kullanıcı şu soruyu sordu:
{question}

Seçilen tarot kartları:
{cards}

Bu kartlara göre mistik bir tarot falı yorumla.
"""

        try:

            response=client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role":"user","content":prompt}]
            )

            yorum=response.choices[0].message.content

        except Exception as e:

            yorum="🔮 Fal şu anda yorumlanamıyor. Lütfen tekrar deneyin."

    return render_template("index.html",yorum=yorum,cards=cards)

if __name__=="__main__":
    app.run()
