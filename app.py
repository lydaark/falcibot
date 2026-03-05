from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Fal cevapları
fal_cevaplari = [
"Yakında güzel bir haber alacaksın.",
"Bu konuda biraz sabırlı olman gerekiyor.",
"Şu an doğru zaman değil.",
"Beklenmedik bir fırsat kapını çalabilir.",
"Geçmişten biri tekrar hayatına girebilir.",
"Yeni bir başlangıç görünüyor.",
"İç sesini dinlemelisin.",
"Bir yolculuk görünüyor.",
"Bir dileğin gerçekleşebilir."
]

# Tarot kartları
tarot_kartlari = [
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
"The Star",
"The Moon",
"The Sun"
]

@app.route("/", methods=["GET","POST"])
def index():

    fal_sonucu = ""
    tarot_sonuc = []

    if request.method == "POST":

        # soru falı
        if request.form.get("question"):
            fal_sonucu = random.choice(fal_cevaplari)

        # tarot kartları
        tarot_sonuc = random.sample(tarot_kartlari,3)

    return render_template("index.html",
                           answer=fal_sonucu,
                           tarot=tarot_sonuc)

if __name__ == "__main__":
    app.run(debug=False)
