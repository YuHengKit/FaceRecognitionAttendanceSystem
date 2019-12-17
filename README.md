# Face Recognition Attendance System

![alt homepage](https://github.com/YuHengKit/FaceRecognitionSystem/blob/master/homepage.PNG?raw=true)

<h1>Team HKL</h1>
<p>Members : </p>
<p>1. HAU ZHE XUAN</p>
<p>2. KIT YU HENG</p>
<p>3. LIM JUN SHIUN</p>

## Overview

A face recognition based attendance system with Raspberry Pi. (Note: At least Raspberry Pi 3 to run smoothly.)

Funtions of the system:
  - Photos Management
  - User Management
  - Recognizer Training
  - Email Notification for Latecomers
  - Attendance Record
  
  
## System Architecture
<img src="https://user-images.githubusercontent.com/11400016/70865130-c93c1400-1f94-11ea-8d47-598a18b3ced9.PNG" />

## Domain Model
<img src="https://user-images.githubusercontent.com/11400016/67187139-2778ca80-f41c-11e9-9e0d-8ac02b5dc316.png" />

## Entity-Relationship Diagram
<img src="https://user-images.githubusercontent.com/11400016/67187172-3b243100-f41c-11e9-8e39-abd7306cb451.png" />


## The recognition module
```__init__.py``` contains the face_cascade object, a common resource used in face detection.

```trainer.py``` is responsible of feeding the dataset to different models for training.

1. Three models are available but unused: ```LBPH, FisherFace``` and ```EigenFace```. The recognizer will compares three results from each model and get the most frequenct result.

2. The system was upgraded with model using ```face_recognition``` library to recognize the face. Only One input image of each user is needed for training purpose. The algorithm of this recognizer is HOG.

```recognizer.py``` uses pretrained models to make predictions.

```capture.py``` adds photos to user profile.


## The django web interface
- Login
<img src="https://user-images.githubusercontent.com/55488934/70975527-14653c80-20e5-11ea-9ded-c7b46c9c59bc.jpg"/>

- Homepage: showing last stats of the system
- Add user: to add new faces
- Capture page: to take faces photos from a local or remote device
- Train page: to train models
- Attendance page: shows attendance records
- A RESTful API interface to send image and attendance records (from the raspberry pi in the prototype device)


## Environment
Python: > 3.6

Install libraries: ```pip3 install -r requirements.txt```


## Running / way to execute
Please create ```photos``` , ```temp``` and ```profile``` folder in static folder.
Please install postgreSQL and change the details in ```setting.py```.
Initialize the database from django:
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

Start the server:
```python3 manage.py runserver```

Reset database:
```python manage.py flush```

<h1>Class Diagram</h1>
<img src="https://user-images.githubusercontent.com/11400016/69170362-eec03400-0b34-11ea-9c4d-0a9aa00d3b3b.png" />

<h1>Database Table</h1>
<img src="https://user-images.githubusercontent.com/11400016/70039481-04cdfa00-15f5-11ea-9fbb-ff192d5572bd.png" />

<h1>Normalized Table</h1>
<img src="https://user-images.githubusercontent.com/11400016/70039442-ecf67600-15f4-11ea-8384-3534617b4e74.PNG" />

