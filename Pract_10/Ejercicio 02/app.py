from multiprocessing.sharedctypes import Value
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


def folderupload():
    folder = request.form['folder']
    if (folder == "Testing"):
        app.config['UPLOAD_FOLDER'] = './static/archivos/testing'
    elif (folder == "DesarrolloWeb"):
        app.config['UPLOAD_FOLDER'] = './static/archivos/desarrolloweb'
    else:
        app.config['UPLOAD_FOLDER'] = './static/archivos/estadistica'
    return (app.config['UPLOAD_FOLDER'])


@app.route("/")
def upload_file():
    return render_template('formulario.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['archivo']
        filename = secure_filename(file.filename)
        pathfolder = folderupload()
        file.save(os.path.join(pathfolder, filename))
        return "<h1>Archivo subido exitosamente</h1>"


if __name__ == '__main__':
    app.run(debug=True)
