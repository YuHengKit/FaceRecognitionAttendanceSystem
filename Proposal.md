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

<p>When the system is activated, camera will keep operate for a period to detect the face and capture it as image. Then, the data of image taken will send to Raspberry Pi to process it to data that need to be send to Cloud Database.</p>
<p>The data of image will saved in Cloud Database that use for data storing. After that, the data stored will send to another Database to go through face recognition process. Data of image will be recognized and classify according to data saved in database. Classified face data will be send to Attendance System Management to data record purpose.</p> 
<p>The data of user such as ID, Name, Check In and Check Out Time will be recorded. If there is a feedback, it will be send to management based on the requirements.</p>

<h1>System Architecture</h1>
<img src="https://user-images.githubusercontent.com/11400016/70865130-c93c1400-1f94-11ea-8d47-598a18b3ced9.PNG" />
