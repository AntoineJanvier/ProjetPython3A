# ProjetPython3A

## Installation
```
$ mkdir projet
$ cd projet/
$ django-admin.py startproject projet_python
$ cd projet_python
$ python manage.py startapp ProjetPython
```

## Run server
```
$ python manage.py runserver
```
> By default, server is running at 127.0.0.1:8000
> To change this, use for example the following command :
```
$ python manage.py runserver 0.0.0.0:1234
```

## Migrations & Classes
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Create superuser
```
$ python manage.py createsuperuser
```

## Configuration
Add "ProjetPython" to "INSTALLED_APPS" in settings.py
> By default, Django uses embedded database, to change this, you must specify it in "settings.py" file too
