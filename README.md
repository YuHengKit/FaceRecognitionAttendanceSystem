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
  - Email Notification for Latecomers (Using ```yagmail``` library)
  - Attendance Record 
  
  
## System Architecture
<img src="https://user-images.githubusercontent.com/11400016/70865130-c93c1400-1f94-11ea-8d47-598a18b3ced9.PNG" />

## Domain Model
<img src="https://user-images.githubusercontent.com/11400016/71082333-e3ac0280-21cb-11ea-90a3-d44a43f54227.png" />

## Entity-Relationship Diagram
<img src="https://user-images.githubusercontent.com/11400016/71082397-01796780-21cc-11ea-935b-981a18522041.png" />

## Class Diagram
<img src="https://user-images.githubusercontent.com/11400016/69170362-eec03400-0b34-11ea-9c4d-0a9aa00d3b3b.png" />

## Database Table
<img src="https://user-images.githubusercontent.com/11400016/70039481-04cdfa00-15f5-11ea-9fbb-ff192d5572bd.png" />

## Normalized Table
<img src="https://user-images.githubusercontent.com/11400016/70039442-ecf67600-15f4-11ea-8384-3534617b4e74.PNG" />

## Initial Sketching of System
<img src="https://user-images.githubusercontent.com/11400016/71343122-d27f3f00-2599-11ea-9239-17f4819b103e.jpg" />

## Recognition Module
```__init__.py``` contains the face_cascade object, a common resource used in face detection.

```trainer.py``` is responsible of feeding the dataset to different models for training.

1. Three models are available but unused: ```LBPH, FisherFace``` and ```EigenFace```. The recognizer will compares three results from each model and get the most frequenct result.

2. The system was upgraded with model using ```face_recognition``` library to recognize the face. Only One input image of each user is needed for training purpose. The algorithm of this recognizer is Histogram of Gradient (HOG).

```recognizer.py``` uses pretrained models to make predictions.

```capture.py``` adds photos to user profile.


## The Django Web Interface
- Login Page
<img src="https://user-images.githubusercontent.com/55488934/70975527-14653c80-20e5-11ea-9ded-c7b46c9c59bc.jpg"/>

- Homepage: showing last stats of the system
<img src="https://github.com/YuHengKit/FaceRecognitionSystem/blob/master/homepage.PNG?raw=true"/>

- Add user: to add new user
<img src="https://user-images.githubusercontent.com/55488934/71083278-99c41c00-21cd-11ea-94de-e246b84d416f.jpeg"/>

- Capture page: to take faces photos from a local or remote device
<img src="https://user-images.githubusercontent.com/55488934/71083168-5e295200-21cd-11ea-9009-de8ae80d286e.jpeg"/>

- Train page: to train models
- Attendance page: shows attendance records
<img src="https://user-images.githubusercontent.com/55488934/71083231-80bb6b00-21cd-11ea-8c96-3a91830ccdab.jpeg"/>

- A RESTful API interface to send image and attendance records (from the raspberry pi in the prototype device)


## Environment
Python: > 3.6

Install libraries: ```pip3 install -r requirements.txt```


## Running / Way to Execute
Please create ```photos``` , ```temp``` and ```profile``` folder in static folder.
Please install postgreSQL and change the details in ```setting.py```.
Initialize the database from django:
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

Start the server:
```python3 manage.py runserver```

Register email:
open a python script in server and run
```import yagmail```
```yagmail.register('mygmailusername', 'mygmailpassword')```
Please change the email address in ```emailalert()``` that can be found in ```views.py```

Reset database:
```python manage.py flush```



