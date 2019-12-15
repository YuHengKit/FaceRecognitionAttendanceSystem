# Face Recognition Attendance System

![alt homepage](https://github.com/YuHengKit/FaceRecognitionSystem/blob/master/homepage.PNG?raw=true)

<h1>Team HKL</h1>
<p>Members : </p>
<p>1. HAU ZHE XUAN</p>
<p>2. KIT YU HENG</p>
<p>3. LIM JUN SHIUN</p>

## Overview

A face recognition based attendence system with Raspberry Pi. (Note: At least Raspberry Pi 3 to run smoothly.)

Python module providing face recognition functionalities:
  - Managing faces photos
  - Training models
  - Making predictions
  
   <h1>System Architecture</h1>
<img src="https://user-images.githubusercontent.com/11400016/70865130-c93c1400-1f94-11ea-8d47-598a18b3ced9.PNG" />


## The recognition module
```__init__.py``` contains the face_cascade object, a common resource used in face detection.

```trainer.py``` is responsible of feeding the dataset to different models for training.

1. Three models are available but unused: ```LBPH, FisherFace``` and ```EigenFace```. The recognizer will compares three results from each model and get the most frequenct result.

2. The system was upgraded with model using face_recognition library to recognize the face. One input image is needed for each user. The algorithm of this recognizer is HOG.

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


## Running / way to execute
Please install postgreSQL and change the details in ```setting.py```.
Initialize the database from django:
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

Start the server:
```python3 manage.py runserver```

Reset database:
```python manage.py flush```
