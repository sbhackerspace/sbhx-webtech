SB Hackerspace's
===============
<br />
#Intro to Django

---

<br />
##Presentor: AJ Bahnken
<br />
##Co-Presentor: Steve Phillips
<br />
##Presented: Jan 18, 2012 @ SB Hackerspace
<br />

---

##What I Hope to Accomplish Tonight

.notes: teach ya

 - Give you a basic overview of Django
 - Get you started on your first Django Project/App
 - Teach you some Django tricks

##Things to note

 - This is only a basic introduction to Django.
 - There are a lot of ways to do a single thing.
 - I recommend looking at more than one Intro to Django tutorial.
---

##What is Django?

Django is a Web Framework written in the Python
programming language. It uses the MVC Structure (kinda).
It is also hugely built on the idea of being clean and promotes
sticking to the DRY (Don't Repeat Yourself) philosophy.

##What is a Web Framework?

frame·work  --  /ˈfrāmˌwərk/

Noun:   
    An essential supporting structure of a building, vehicle, or object.

A Web Framework is a framework (obviously) with the
purpose of supporting development of web sites and web
apps.

.notes: It helps eliminate bullshit dirty work

---

##Why 'MVC (kinda)'?

MVC stands for 'Model View Controller', and it is
an architectural pattern of software design. Django 
does use this, but it is more commonly refered to as
MTV, which stands for 'Model Template View'.

This is because in a 'MVC', the 'View' controls 'what' and 'how'
the data is displayed within the browser, in Django the 'Template'
controls 'how', and the Views control 'what'.

---

##Who's using Django?

Some with a lot of traffic:

 - [Disqus](http://disqus.com/) -- online discussion and commenting service for websites and online communities. (500 Million monthly users)
 - [Bitbucket](https://bitbucket.org/) -- a web-based hosting service for projects that use either the Mercurial or Git revision control systems.
 - [Giant Bomb](http://www.giantbomb.com/) -- (lame) Video Game Reviewing site
 - [User Echo](http://userecho.com/) -- a site for user to owner communication. Feedback, etc.
 - [The Onion](http://www.theonion.com/) -- greatest news network ever, of course.
 - [Washington Post](washingtonpost.com)

---

#Questions yo?

---

##Extra Tools Being Used

##VirtualEnv

VirtualEnvWrapper allows you to setup a separate
enviorment for development and production so you can
have different versions of softwares (such as Django)
on one machine. This makes sure you don't break everything.

##pip

pip is Python's packagemanager (Similar to apt-get, aptitude, pacman, etc).
Its nothing special, but you should get used to using it. Tools such as search
and freeze are really helpful and can be important.

##My env

Just as a reference incase you are confused by my env, I am running Ubuntu 11.04,
with awesome as my window manager, urxvt+byobu as my terminal emulator, and vim as my IDE.

---

##A Django project.

    !bash
    django-admin.py startproject 'project_name'

##This generates a folder with:
    
    !bash
    __init__.py

Makes the folder a package, which allows it to
be callable within a terminal. Important.

##manage.py

Controls a lot of the functionality of Django.
This (and '__init__.py') you won't really have to touch.

---
## Along with

##urls.py

Controls URL declarations for your Django Project and each
individual Django App. (As quoted from Django's official tutorial,
"'Table of contents' of your Django-powered site"

##setting.py

Settings for your Django Project. This is the main configuration
file.

---
##Quick note

The 'T' in 'MTV' stands for 'Template', right?

Well what this means is there is a seperate folder within your
Django Project that will hold HTML templates. These HTML files
are in essence the same as typical HTML files, but also include
Django 'Template Tags'. 

---

#Let's take a look at the code...

---

##Two 'settings.py' tricks

##Working Locally

A big thing with 'settings.py' is that all of the file paths
are going to be specific to each machine. This throws A LOT of
problems when multiple people are working on your Django Project/App.
A great way of getting around this is...

    !python
    import os
    PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

    'NAME': os.path.join(PROJECT_PATH, 'db.sql'),

Another big problem when working on a Django Project locally vs server-side
is specific settings that can break the site completely. A common one is SQLite3 vs
MySQL/Postgres. Using a settings_local.py is really helpful for this.

    !python
    try:
         from settings_local import *

---

#Questions yo?

---

##A Django App

Once you have a Django Project created, you are
going to wanna actually write an app, right?

While you are in your folder:


    !bash
    python manage.py startapp 'app_name'

This will create a folder with
    
    !bash
    __init__.py
    tests.py

A file for creating and running unittests and doctests.
(We probably won't cover this that much in this talk)

---

##models.py

Python Classes that outline and define the structure of the data
that will be stored. Basically your database layout.

    !python
    class Publisher(models.Model):
        name = models.CharField(max_length=30)
        address = models.CharField(max_length=50)
        city = models.CharField(max_length=60)
        state_province = models.CharField(max_length=30)
        country = models.CharField(max_length=50)
        website = models.URLField()
    
    class Author(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=40)
        email = models.EmailField()
                
    class Book(models.Model):
        title = models.CharField(max_length=100)
        authors = models.ManyToManyField(Author)
        publisher = models.ForeignKey(Publisher)
        publication_date = models.DateField()



---

#views.py

The main functionality of your App. This utilizes each Model,
along with determining what data is displayed.

    !python
    from django.shortcuts import render_to_response
    import datetime

    def hello(request):
        return HttpResponse("Hello world")

    def current_datetime(request):
        current_date = datetime.datetime.now()
        return render_to_response('current_datetime.html', locals())



---

#Lets take a look at the code...

---

#References

 - https://docs.djangoproject.com/en/1.3/ 
 - http://en.wikipedia.org/wiki/Django
 - http://jeffcroft.com/blog/2007/jan/11/django-and-mtv/
 - http://www.djangosites.org/
 - http://www.slideshare.net/zeeg/pycon-2011-scaling-disqus-7251315
