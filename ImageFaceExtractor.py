#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

import OpenCVGenericDetection

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    genericClass = OpenCVGenericDetection.OpenCVGenericDetection(
        image_path = './img/visage.jpg',
        archive_folder = './archive', 
        debug = True
        )

