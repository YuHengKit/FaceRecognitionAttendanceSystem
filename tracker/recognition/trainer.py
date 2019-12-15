#!/usr/local/bin/python3

import os
import face_recognition
import cv2
import numpy as np
#from tracker.models import User
import yaml
from tracker.recognition import face_cascade


class Trainer:
    """
    The trainer class is the responsible of reading datasets, training them, and exporting the trained model
    """

    def __init__(self, photos, export):
        """
        Initialization of attributes
        :param photos: The directory containing photos to be trained on
        :param export: The path where the trained model will be saved
        """
        self.photos = photos
        self.export = export

    def get_nbr_photos(self):
        try:
            return len(os.listdir(self.photos))
        except: return 'None'

    def get_photo_size(self):
        return 100,100
        if len(os.listdir(self.photos)) == 0:
            return None, None
        image_paths = [os.path.join(self.photos, f) for f in os.listdir(self.photos)]
        image_pil = cv2.imread(image_paths[0])
        gray = cv2.cvtColor(image_pil, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        width, height = faces[0][2:4]
        for image_path in image_paths:
            image_pil = cv2.imread(image_path)
            gray = cv2.cvtColor(image_pil, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.3,minNeighbors = 4)
            try:
                x, y, w, h = faces[0]
                if w < width: width = w
                if h < height: height = h
            except:
                continue
        return width, height

    def get_images_and_labels(self, same_size=False):
        image_paths = [os.path.join(self.photos, f) for f in os.listdir(self.photos)]
        images, labels = [], []
        if same_size:
            width, height = self.get_photo_size()
        for image_path in image_paths:
            image_pil = cv2.imread(image_path)
            try:
                nbr = int(os.path.split(image_path)[1].split("_")[0])
            except:
                continue
            gray = cv2.cvtColor(image_pil, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.3,minNeighbors = 4)
            image = np.array(gray, 'uint8')
            for x, y, w, h in faces:
                if same_size:
                    resized = cv2.resize(image[y:y + h, x:x + w], (width, height))
                    images.append(resized)
                else:
                    images.append(image[y:y + h, x:x + w])
                labels.append(nbr)
        return images, np.array(labels)

#   def train(self):
#        """
#        Trains a model from dataset, saves the file to export path
#        This process may take several minutes, make sure you have an SSD!
#        :return: 
#        """
#        # create the face recognizer object
#        lbph_rec = cv2.face.LBPHFaceRecognizer_create()
#        eigenface_rec = cv2.face.EigenFaceRecognizer_create()
#        fisherface_rec = cv2.face.FisherFaceRecognizer_create()

#        # Train LBPH recognizer
#        images, labels = self.get_images_and_labels()
#        lbph_rec.train(images, labels)
#        lbph_rec.save(self.export + '_lbph.yml')

#        # Train other two recognizers
#        images, labels = self.get_images_and_labels(same_size=True)
#        for recognizer, name in zip((eigenface_rec, fisherface_rec), ('eigenface', 'fisherface')):
#            recognizer.train(images, labels)
#            recognizer.save(self.export + '_' + name + '.yml')

    def train(self):
        self.known_faces=[]
        for i in range(len(os.listdir(self.photos))):
            image = face_recognition.load_image_file("static/photos/"+str(i+1)+"_0.png")
            #print(i)
            k=face_recognition.face_encodings(image)[0]
            #print(k)
            self.known_faces.append(k)
            #print(self.known_faces)
        with open(r'static/trained.yaml', 'w') as file:
            documents = yaml.dump(self.known_faces, file)
        return self.known_faces
