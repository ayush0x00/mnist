from flask import Flask,render_template,request
import numpy as np
from PIL import Image
#from scipy.misc import imresize
from keras.models import load_model
import re,os,base64,sys
import numpy as np
import tensorflow as tf

app=Flask(__name__)
global model,graph
graph=tf.compat.v1.get_default_graph()
model=load_model("model/mnist.h5")
def parse_image(image_string):
    imgstr=re.search(b'base64,(.*)',image_string).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))
def process_image(image):
    image=np.resize(image,(28,28))
    im=image.reshape(1,28,28,1)
    return tf.cast(im,dtype=tf.float32)/255.0

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def display_result():
    parse_image(request.get_data())
    im=np.array(Image.open('output.png'))
    im=process_image(im)
    #im=im.reshape(1,28,28,1)
    #with tf.Graph().as_default():
        #out=model.predict(im)
        #print(np.argmax(out,axis=1))
    #print(im.shape)
    print(model.summary())
    return "Model summay loaded"
