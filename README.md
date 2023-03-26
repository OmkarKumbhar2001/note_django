# note_django
How to create Project ===>   python -m django startproject project_name <br>
here project name => Hello<br>
cd Hello <br>
python manage.py runserver <br>
Open => http://127.0.0.1:8000/<br>
<hr>
Create app ==>python manage.py startapp home <b><em>home is name of app</em></b> <br> 
Static file  http://127.0.0.1:8000/static/test.txt <br>
<hr>
<b>Where to add templates file</b><br>
dir => Hello(<em>Inside Project file</em>)=> settings.py TEMPLATES(<em>TEMPLATES(array)=>DIRS=["you can store here templates file location"]</em>)<br>
current file =DIRS=[BASE_DIR / "static",]
<hr>
