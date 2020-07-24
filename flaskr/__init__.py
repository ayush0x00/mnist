from flask import Flask,render_template,jsonify,request,send_file
from flask_sqlalchemy import SQLAlchemy
import json,base64
import re
import numpy as np
from PIL import Image
import os,sys

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:user@localhost:5432/mnistdb'
db=SQLAlchemy(app)

class Person(db.Model):
    __tablename__="image"
    id=db.Column(db.Integer,primary_key=True)
    image_string=db.Column(db.String(),nullable=False)
db.create_all()

def renderblog():
    filename = os.path.join(app.static_folder, 'model/model.json')
    with open(filename) as blog_file:
        model = json.load(blog_file)
def parseImage(imgData):
    # parse canvas bytes and save as output.png
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    return base64.decodebytes(imgstr)

@app.route("/",methods=['GET'])
def welcome():
    print("Rendering model",file=sys.stdout)
    renderblog()
    return render_template("index.html")


@app.route("/send",methods=['GET','POST'])
def printing():
    image_send= parseImage(request.get_data())
    return base64.encodebytes(image_send)
