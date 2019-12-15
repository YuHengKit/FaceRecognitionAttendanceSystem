#!/usr/local/bin/python3
import yaml
import cv2
import numpy as np
from collections import Counter
import face_recognition
from tracker.recognition.trainer import Trainer
from tracker.recognition import face_cascade
from PIL import Image


class Recognizer:
    """
    The recognizer class contains a recognizer object that predicts the label of a given photo
    Several methods are included such as reading an image from disk, from video source, from a URL, searching in social
    media...
    """

    def __init__(self, recognizer_filename, source, max_width, max_height, threshold=None):
        """
        Initialization of attributes
        :param recognizer_filename: Path of the file containing the exported trained model
        :param source: Video source to read from in case of reading from a camera
        :param threshold: Threshold between recognizing and not recognizing an input photo
        """
        photos_path = 'static/photos'
        train_file_name = 'static/trained'
        #self.trainer=Trainer(photos_path,train_file_name)
        trainer=Trainer(photos_path,train_file_name)
        self.known_faces=trainer.train()

        #self.known_faces=trainer.train()
        self.recognizer_filename = recognizer_filename
        self.source = source
        self.video_capture = None
        self.max_width = max_width
        self.max_height = max_height
        #self.lbph_rec = self.eigenface_rec = self.fisherface_rec = None
        #self.reload()C:\Users\Heng1222\Desktop\tracker-master\tracker-master\static\photos
        self.lbph_rec = cv2.face.LBPHFaceRecognizer_create()
        self.eigenface_rec = cv2.face.EigenFaceRecognizer_create()
        self.fisherface_rec = cv2.face.FisherFaceRecognizer_create()
        self.lbph_rec.read("static/trained_lbph.yml")
        self.eigenface_rec.read("static/trained_eigenface.yml")
        self.fisherface_rec.read("static/trained_fisherface.yml")




    def reload(self):
        self.lbph_rec = cv2.face.LBPHFaceRecognizer_create()
        self.eigenface_rec = cv2.face.EigenFaceRecognizer_create()
        self.fisherface_rec = cv2.face.FisherFaceRecognizer_create(2)
        #for recognizer, name in (
        #        (self.lbph_rec, 'lbph'), (self.eigenface_rec, 'eigenface'), (self.fisherface_rec, 'fisherface')):
        #    try:
        #        recognizer.load(self.recognizer_filename + '_' + name + '.yml')
        #        print("Done Loading!")
        #    except:
        #        pass

    def open_source(self):
        """
        Opens the source of video
        :return: 
        """
        self.video_capture = cv2.VideoCapture(self.source)

    def read_image(self):
        """
        Read a single image from the source
        :return: A tuple containing the original image and a greyscale version of it
        """
        self.open_source()
        image = np.array(self.video_capture.read()[1])
        return image, cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 #   def predict(self, *grays):
   #     res = []
        #print("Start Predict")

    #    for gray in grays:
            #print("Stage 1")
    #        faces = face_cascade.detectMultiScale(gray)
     #       #print("Face Detected")
      #      #print(faces)
      #      for (x, y, w, h) in faces:
      #          if self.lbph_rec is not None:
      #              try:
                        #print("OMG")
      #                  output=self.lbph_rec.predict(gray[y: y + h, x: x + w])
                        #print(output)
      #                  res.append(output)
                        #print("haha")
                        #print(res)
      #              except:
                        #print("No")
      #                  res.append(None)
      #      for recognizer in (self.eigenface_rec, self.fisherface_rec):
                #print("stage2")
      #          faces = face_cascade.detectMultiScale(gray)
      #          for (x, y, w, h) in faces:
      #              img = gray[y: y + h, x: x + w].copy()
      #             img = cv2.resize(img, (self.max_width, self.max_height))
      #              if recognizer is not None:
      #                  try:
      #                      #print("Stage3")
      #                      out=recognizer.predict(img)
      #                      res.append(out)
                            #print("hahaha")
                            #print(res)
      #                  except:
                            #print("NONO")
      #                      res.append(None)
      #  if not res: return None, None
      #  if len(res) < len(grays) * 3:
      #      for i in range(len(grays) * 3 - len(res)):
      #          res.append(None)
      #  top, occur = Counter(res).most_common(1)[0]
      #  print(occur)
      #  percent = int((top[1]))
      #  print(percent)
      #  print(top)   
      # return int(top[0]), int(percent)'''

    def predict(self, *grays):
        with open(r'static/trained.yaml') as file:
            documents = yaml.load(file, Loader=yaml.Loader)
        self.known_faces=np.array(documents)
        print(self.known_faces)
        face_locations = []
        face_encodings = []
        match=[]
        for gray in grays:
                faces = face_cascade.detectMultiScale(gray)
                for (x, y, w, h) in faces:
                      img = gray.copy()
                      img = Image.fromarray(img).save('static/temp/User.png')
                      img1 = face_recognition.load_image_file("static/temp/User.png")       #load image that need to be processed
                      face_locations = face_recognition.face_locations(img1, model='hog')
                      face_encodings = face_recognition.face_encodings(img1, face_locations)
    
        for face_encoding in face_encodings:   #face recognition start
                match = face_recognition.compare_faces(self.known_faces, face_encoding, tolerance=0.30)
        print(match)
        id=0
        for i in range(len(match)):
            if match[i]==True:
                id = i+1
            else:
                pass

        print(id)
        percent=100
        return int(id), int(percent)

    def get_image_label(self, *paths):
        """
        Gets the label of a saved photo on the disk
        :param path: Path of the photo
        :return: The predicted label of the photo
        """
        grays = []
        for path in paths:
            image1=cv2.imread(path)
            image = np.array(image1)
            gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            grays.append(gray)
        #print("Done get image label")
        #print(grays)
        return self.predict(*grays)

    def recognize_from_video(self, num=10):
        """
        A generator the predicts the label of photos read from video source
        :param num: Number of iterations
        :return: The prediction of the photo
        """
        for i in range(num):
            image, gray = self.read_image()
            yield self.predict(gray)

    def get_label(self):
        for i in range(5):
            image, gray = self.read_image()
            yield self.predict(gray)

    def save_and_get_label(self):
        for i in range(5):
            self.read_image()
        grays, paths = [], []
        for i in range(5):
            grays.append(self.read_image()[1])
        for i, gray in enumerate(grays):
            faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.3,minNeighbors = 4)
            for (x, y, w, h) in faces:
                paths.append('img' + str(i) + '.jpg')
                cv2.imwrite(paths[-1], gray[y:y + h, x:x + w])
        return self.get_image_label(*paths)

    def resize_image(self, path, width, height):
        img = cv2.imread(path)
        img = cv2.resize(img, (width, height))
        cv2.imwrite(path, img)
