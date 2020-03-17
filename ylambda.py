from flask import Flask
from flask import request

from io import BytesIO
import PIL.Image

import aiohttp
import asyncio

import os

from fastai.vision import *


app = Flask(__name__)


##################### Loading Changes ##############################################################
####################################################################################################
#to restart after changes
# sudo service nginx restart
# sudo service ylambda restart
#to live reload from debugging to production place this in ylambda.ini
# touch-reload = /home/elliot/ylambda/ylambda.py


##################### Y Lambda Homagepage ##########################################################
####################################################################################################

@app.route("/")
def homepage():
    return "Welcome to YLambda"

############################# PRXMTY ###############################################################
####################################################################################################

@app.route("/prxmty")
def prxmtyHomepage():
    return "Welcome to Prxmty"

@app.route("/prxmty/<test_response>")
def prxmtyTest(test_response):
    return ({"Prxmty Response": test_response})

############################## Recylce.ai ##########################################################
####################################################################################################

@app.route('/recycleai')
def recycle_ai():
    return "Welcome to Recycle.ai"

################### Grabbing Local Image File ##############################

@app.route('/recycleai/upload', methods=['POST'])
def recycle_ai_classify():

    name = request.form['name']
    #Grab Image from Post Form
    img = request.files['image']
    img = open_image(BytesIO(img.read()))
    #classify Image
    learner = load_learner(Path("./"))
    _,_,losses = learner.predict(img)

    return ({
        "predictions": sorted(
            zip(learner.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True)})



############################## Run Flask Application ##########################################################
####################################################################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0')
