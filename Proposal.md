<!DOCTYPE html>
<html>

<h1>Title</h1>
<body>Face Recognition Attendance System</body>


<h1>Team HKL</h1>
<p>Members : </p>
<p>1. HAU ZHE XUAN</p>
<p>2. KIT YU HENG</p>
<p>3. LIM JUN SHIUN</p>

<h1>Overview</h1>

<p>When the system is activated, camera will keep operate for a period to detect the face and capture it as image. Then, the data of image taken will send to Raspberry Pi to process it to data that need to be send to Database.</p>
<p>The data of image will saved in Database that use for data storing. After that, the data stored will send to another Database to go through face recognition process. Data of image will be recognized and classify according to data saved in database. Classified face data will be send to Attendance System Management to data record purpose.</p> 
<p>The data of user such as ID, Name, Check In and Check Out Time will be recorded. If there is a feedback, it will be send to management based on the requirements.</p>

## System Architecture
<img src="https://user-images.githubusercontent.com/11400016/70865130-c93c1400-1f94-11ea-8d47-598a18b3ced9.PNG" />

## Domain Model
<img src="https://user-images.githubusercontent.com/55488934/71083649-7baaeb80-21ce-11ea-8ad9-2909ace76bf3.png" />

## Entity-Relationship Diagram
<img src="https://user-images.githubusercontent.com/55488934/71083676-88c7da80-21ce-11ea-9032-26095b28cf89.png" />

## Database Tables
<img src="https://user-images.githubusercontent.com/11400016/70039481-04cdfa00-15f5-11ea-9fbb-ff192d5572bd.png" />

## Class Diagram
<img src="https://user-images.githubusercontent.com/11400016/69170362-eec03400-0b34-11ea-9c4d-0a9aa00d3b3b.png" />

## User Interface
- Login Page
- Homepage: showing last stats of the system
- Add user: to add new user
- Capture page: to take faces photos from a local or remote device
- Train page: to train models
- Attendance page: shows attendance records
- A RESTful API interface to send image and attendance records (from the raspberry pi in the prototype device)

## Normalized Table
<img src="https://user-images.githubusercontent.com/11400016/70039442-ecf67600-15f4-11ea-8384-3534617b4e74.PNG" />
