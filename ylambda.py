from flask import Flask
from flask import request

from io import BytesIO
import PIL.Image

import aiohttp
import asyncio
import json

import os
import sys



#Import Prxmty Main Function
sys.path.insert(1, './prxmty')
from prxmty import prxmty_main

#Import Recycle.ai Main Function
sys.path.insert(1, './recycleai')
from recycleai import recycleai_main



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

# @app.route("/prxmty/test")
# def prxmtyTest():
#     #grab popular times response
#     response = prxmty_main()
#
#     return ({"Prxmty Response": response})

@app.route("/prxmty/rectangle", methods=['POST'])
def prxmtyRectangle():

    #grab southwest_corner and northeast_corner fields
    southwest_corner = json.loads(request.form['southwest_corner'])
    northeast_corner = json.loads(request.form['northeast_corner'])

    # #grab popular times response
    response = prxmty_main(southwest_corner,northeast_corner)

    return ({"Prxmty Response": response})

############################## Recylce.ai ##########################################################
####################################################################################################

@app.route('/recycleai')
def recycle_ai():
    return "Welcome to Recycle.ai"

################### Grabbing Local Image File ##############################

@app.route('/recycleai/upload', methods=['POST'])
def recycle_ai_classify():

    #grab example name field
    name = request.form['name']
    #Grab Image from Post Form
    img = request.files['image']

    #classify image
    response = recycleai_main(img)

    return response



############################## Run Flask Application ##########################################################
####################################################################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0')
