import cv2
import numpy as np


class FaceDetector(object):
    """ Detect faces in an image using OpenCV's Haar Cascade

    :param face_cascade: pre-trained face classifier
    """

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    

    def detect_cascade(self, image):
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        return len(faces)


    def face_count(self, image):
        faces = self.detect_cascade(image)

        return faces