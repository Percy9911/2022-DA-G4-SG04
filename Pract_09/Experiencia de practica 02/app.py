from flask import Flask 

#@app.route("/") 
#def home():
#   return "Hello, Flask!"

from flask import render_template 
app = Flask(__name__)
@app.route('/') 
#@app.route('/index')
def index():

    usuario = {'nombre':'fede'}
    pubs = [
        {
            'autor': {'usuario': 'Juan'},
            'pub': 'Bonito dia en Barcelona'
        },
        {
            'autor': {'usuario': 'Maria'},
            'pub': 'Hoy ta buena tarde enuve un el cine'
        },
    ]
    return render_template('index.html', titulo="Inicio", usuario=usuario)