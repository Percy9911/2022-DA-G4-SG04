from flask import Flask, render_template
from artist import Artist
from cont import Cont

app = Flask(__name__)


lst_Art = [
    Artist('Taylor Swift', 32, 'F', 17, 'img/taylor.jpg'),
    Artist('Shawn Mendes', 24, 'M', 4, 'img/shawn.jpg'),
    Artist('Ariana Grande', 29, 'F', 6, 'img/ariana.jpg')
]


listCont = [
    Cont('insta.com', '+51 912 233 843', 'artist@gmail.com')
]


@app.route("/")
def inicio():
    return render_template('artist.html', artists=lst_Art)


@app.route("/contact")
def contact():
    return render_template('contact.html', contac=listCont)
