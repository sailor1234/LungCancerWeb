import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import numpy as np
import tensorflow as tf

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/lezardvaleth/myproject/flask/filestorage.db"
db = SQLAlchemy(app)

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")

def index():
    return render_template("upload.html")

@app.route("/upload", methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print (destination)
        file.save(destination)

    newFile = FileContents(name=file.filename, data = file.read())

    db.session.add(newFile)
    db.session.commit()

    return 'Save ' +file.filename + ' to the database!'


    return render_template("complete.html")



if __name__ == "__main__":
    app.run(port = 4555, debug=True)
