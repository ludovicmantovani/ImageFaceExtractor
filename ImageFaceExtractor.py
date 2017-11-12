#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from OpenCVGenericDetection import *

class OpenCVFaceFrontalDetection(OpenCVGenericDetection):
    def set_classifier(self):
        self.classifier = cv2.CascadeClassifier(FACE_FRONTAL_CLASSIFIER_FILE)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    faceFrontalClass = OpenCVFaceFrontalDetection(
        image_path = './img/visage.jpg',
        archive_folder = './archive/', 
        debug = True
        )

