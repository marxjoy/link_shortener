# Application for shorting links

## 
* [General info](#general-info)
* [Setup](#setup)
* [Technologies](#technologies)

## General info
Application for shorting links




## Setup
Install requirements 
```
pip3 install -r requirements.txt
```
Make migrations
```
python manage.py makemigrations
python manage.py migrate
```


Run server:
```
python manage.py runserver
```

## Technologies
Project is created with:
* Django==2.2
* Django Rest Framework==3.10.3


Database:
* SQLite
