import base64

from flask import Flask, request

from face_recognition import face_detector as fd
from api import app


@app.route('/', methods=['GET'])
def index():
    return "Hello World"


@app.route('/countFaces', methods=['POST'])
def count_faces():
    data = request.get_json()
    img = data['image']
    img = base64.decodestring(img)

    detector = fd.FaceDetector()

    return detector.face_count(img)