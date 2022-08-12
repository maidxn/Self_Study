# Some commands

* **pip install virtualenvwrapper-win** - install the module that creates virtual enviroment

* **mkvirtualenv *name_of_enviroment*** - create a virtual enviroment which has *name*

After creating the VE (virtual enviroment), has to re-install every neccessary modules. Because the VE just likes a box, we put everything we create for ONLY THE PROJECT we're working on.

* Check if you are in the VE or not!

Already in VE 
![After]()

Hasn't yet
![Before]()

* **django-admin startproject *name_of_project*** - cteate a new Django project

Remeber to **cd *name_of_project*** - change directory to that new folder

* **deactivate** - deactivate VE
* **workon *name_of_VE*** - activate VE again
* **python manage.py startapp *name_of_app*** - create a new app
* **python manage.py runserver** - run django project
* **ctrl+C** - quit the server

***context*** - a variable name in views.py file, it like a dictionary which stores are variables you want to send to index.html file.

Remember to send it like a parameter after 'index.html' file - the one you want to render, then *context*

Cross-site request forgery 

POST method: use when you send private information

GET method: use when the information is not so personal

* ***{% csrf_token%}** - in .html files* - allow you to use POST method.

Friendly reminder: If you can't load css, check typo in link 'stylesheet' ;;-;; and add type="text/css" (if you want, i realized it not necessary now) :v.

[Free html template website" *bootstrapmade*](https://bootstrapmade.com/)

Friendly reminder #2: Press Alt + Click on the lineS you want to edit in visual studio code. It's great!

* **python manage.py makemigrations** - this command like it saves all changes in models.py (when create a class/object to use in database). Like you add files and commit in git
* **python manage.py migrate** - like you push all things to the database
These 2 step are necessary to make ANY CHANGES in models.py file

* **python manage.py createsupperuser** - create admin usser to access to */admin* page
username: maidgxn/ Pass: XuanMai0520

 

