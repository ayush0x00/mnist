from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import json
import pickle
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


@app.route("/",methods=['GET'])
def welcome():
    print("Rendering model",file=sys.stdout)
    renderblog()
    return render_template("index.html")

@app.route("/send",methods=['POST'])
def printing():
    # received_string=request.args.get('image_string')
    name = request.form['name']
    return render_template("welcome.html", data=name)