from mlapp import model_mongodb
from flask import Blueprint, current_app, redirect, request, session, url_for,send_file
from io import BytesIO
import numpy as np
from . import storage
import cv2,requests,base64
from werkzeug.datastructures import FileStorage
import requests,pymongo
import json
import sys, os
sys.path.append('..')

from keys import *

crud = Blueprint('crud', __name__)
def upload_image_file(file):

    if not file:
        return None

    public_url = storage.upload_file(
            file.read(),
            file.filename,
            file.content_type
            )
    return public_url

@crud.route("/upload", methods=['POST'])
def process():


    patientid = str(request.form['id'])
    #image_url = upload_image_file(request.files.get('image'))
    if request.files.get('image') is not None:
        img_stream = BytesIO(request.files.get('image').read())
        img = cv2.imdecode(np.fromstring(img_stream.read(), np.uint8),cv2.IMREAD_UNCHANGED)

        resized_image = cv2.resize(img, (256, 256))
        is_success, buffer2 = cv2.imencode(".png", resized_image)
        png_as_text = base64.b64encode(buffer2)

        data = { 'base64' : png_as_text }

        sgmakeresponse = requests.post('https://www.placeholder.com/api', json = data)



    return 'data' 

@crud.route("/patient/<id>", methods=['GET'])
def get(id):
    myclient = pymongo.MongoClient(mongo)
    mydb = myclient[mongodb]
    mycol = mydb[mongocol]

    patient = mycol.find_one({id : {'$exists': True}})
    patient = patient[id]
    return json.dumps({id : patient})



