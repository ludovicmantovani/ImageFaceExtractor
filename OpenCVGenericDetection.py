#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2

class OpenCVGenericDetection:

    def __init__(self, image_path, archive_folder = '/tmp/', debug = False):
        """ Constructeur de la classe
            @image_path : chemin d'une image sur à analyser
            @archive_folder : répertoire d'archive
            @debug : si True, affichage des images dans une fenêtre
        """
        pass

    def set_classifier(self):
        """ Méthode à surcharger
        """
        pass

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
