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
current file =DIRS=[BASE_DIR / "templates",]
<hr>
<b>Admin Panel</b><br>
Run this command to migrate file
python manage.py migrate<br>
Create Super User<br>
python manage.py createsuperuser<br> 
Username (leave blank to use 'omkar'): admin <br>
Email address: set empty<br>
Password:admin<br>
Password (again):admin<br>
Bypass password validation and create user anyway? [y/N]: y<br>
now you can Open<br>
http://127.0.0.1:8000/admin/
User name = admin <br>
password =admin   <br>
<b>How to Change Django administration name</b><br>
add these tags inside project Hello=> urls.py
admin.site.site_header = "Omkar Project" <br>
admin.site.site_title = "Admin Omkar Django Project" <br>
admin.site.index_title = "Hello Omkar" <br>
<hr>
Template inheritance<br>
we can use base.html as a main html file for navbar and footer<br>
{% extends 'base.html' %}<br>
{%block title%}  this code only paste in each html file<br>
    Home page title <br>
{%endblock title%}  <br>
{%block body%}  this code only paste in each html file<br>
    modified code for each file we can store here<br>
{%endblock body%} <br>
for refrence you can check teplates folder<br>