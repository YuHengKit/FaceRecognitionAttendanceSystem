# Face Recognition Attendance System

![alt homepage](https://github.com/YuHengKit/FaceRecognitionSystem/blob/master/homepage.PNG?raw=true)

## Overview

A face recognition based attendence system with Raspberry Pi. (Note: At least Raspberry Pi 3 to run smoothly.)

Python module providing face recognition functionalities:
  - Managing faces photos
  - Training models
  - Making predictions

## The recognition module
```__init__.py``` contains the face_cascade object, a common resource used in face detection.

```trainer.py``` is responsible of feeding the dataset to different models for training.
Three models are available: ```LBPH, FisherFace``` and ```EigenFace```.
The recognizer will compares three results from each model and get the most frequenct result.

```recognizer.py``` uses pretrained models to make predictions.

```capture.py``` adds photos to user profile.


## The django web interface
- Login
- Homepage: showing last stats of the system
- Add user: to add new faces
- Capture page: to take faces photos from a local or remote device
- Train page: to train models
- Attendence page: shows attendence records
- A RESTful API interface to send image and attendence records (from the raspberry pi in the prototype device)


## Environment
Python: > 3.6

Install libraries: ```pip3 install -r requirements.txt```


## Running
Please install postgreSQL and change the details in ```setting.py```.
Initialize the database from django:
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

Start the server:
```python3 manage.py runserver```

Reset database:
```python manage.py flush```
