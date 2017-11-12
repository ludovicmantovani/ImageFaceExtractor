#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import cv2
import logging
import datetime

FACE_FRONTAL_CLASSIFIER_FILE = "./classifier/haarcascade_frontalface_default.xml"
FACE_PROFILE_CLASSIFIER_FILE = "./classifier/haarcascade_profileface.xml"
BODY_FULL_CLASSIFIER_FILE = "./classifier/haarcascade_fullbody.xml"

MAX_SIZE = 800  #Taille maximale de l'image en pixels

class OpenCVGenericDetection:

    def __init__(self, image_path, archive_folder = '/tmp/', debug = False):
        """ Constructeur de la classe
            @image_path : chemin d'une image sur à analyser
            @archive_folder : répertoire d'archive
            @debug : si True, affichage des images dans une fenêtre
        """
        #Vérification validité chemin image et répertoire d'archive
        if image_path == '' or ( not os.path.isfile(image_path)):
            logging.error("Le chemin de l'image [{0}] n'est pas valide.".format(image_path))
            sys.exit(1)
        else:
            logging.info("Image : {0}".format(image_path))
        if archive_folder == '' or ( not os.path.isdir(archive_folder)):
            logging.error("Le chemin du répertoire d'archive [{0}] n'est pas valide.".format(archive_folder))
            sys.exit(1)
        else:
            logging.info("Archive : {0}".format(archive_folder))

        #Initialisation des variables de la classe
        self.image_path = image_path
        self.archive_folder = archive_folder
        self.debug = debug
        self.items = []
        self.items_frames = []

        #Initialisation du classifier
        self.set_classifier()

        #Création du préfix de nomage des images
        self.prefix = "{0}_{1}".format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f"), self.__class__)

        #Chargement de l'image dans une frame
        self.frame = cv2.imread(image_path)
        logging.info("Résolution de l'image : {0}x{1}".format(self.frame.shape[0], self.frame.shape[1]))

        #Réduction de la taille de l'image si besoin
        ratio = 1
        if self.frame.shape[1] > MAX_SIZE or self.frame.shape[0] > MAX_SIZE:
            if self.frame.shape[1] / MAX_SIZE > self.frame.shape[0] / MAX_SIZE:
                ratio = float(self.frame.shape[1]) / MAX_SIZE
            else:
                ratio = float(self.frame.shape[0]) / MAX_SIZE
        if ratio !=1:
            newsize = (
                int(self.frame.shape[1] / ratio),
                int(self.frame.shape[0] / ratio)
            )
            self.frame = cv2.resize(self.frame, newsize)
            logging.info("Redimensionnement de l'image : {0}x{1}".format(self.frame.shape[0], self.frame.shape[1]))
        
        #Affichage de l'image (si debug)
        if self.debug:
            cv2.imshow("preview", self.frame)
            cv2.waitKey()

    def set_classifier(self):
        """ Méthode à surcharger (selection du classifier)
        """
        self.classifier = None

    def find_items(self):
        """ Trouver les items dans une frame
        """
        pass

    def extract_items_frames(self):
        """ Extraire les frames des items de la frame complète
        """
        pass

    def get_items_frames(self, grayscale=False):
        """ Retourne les frames des items et leurs coordonnées dans une liste
            @grayscale : Si True, retourne les frames en niveau de gris
        """
        pass

    def add_label(self, text, x, y):
        """ Ajout d'un label sur la frame complète
            @text : texte à afficher
            @x, y : coordonnées du texte à afficher
        """
        pass

    def archive_items_frames(self):
        """ Ecrit dans le répertoire d'archive chaque frame de chaque item en tant q'une image
        """
        pass

    def archive_with_items(self):
        """ Ecrit dans le répertoire d'archive la frame complète avec les carrés dessinés autour des visages détectés
        """
        pass
