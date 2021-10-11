# Simple Url Shortener

![img](https://visitor-badge.laobi.icu/badge?page_id=ethmtrgt.url_shortener)
![img](https://img.shields.io/github/issues/ethmtrgt/url_shortener)
![img](https://img.shields.io/github/last-commit/ethmtrgt/url_shortener)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)
![GitHub Repo stars](https://img.shields.io/github/stars/ethmtrgt/url_shortener?style=social)

<br>

## What is that?
Yet another url shortener built with Django framework.

<br>

## Preview
![image](https://user-images.githubusercontent.com/48857416/136834823-07ae633a-94f5-439a-bb06-c2a5c5e1bed9.png)

<br>

## HOW TO RUN?
### 1. Virtual Environment
First create a virtual environment by running this command.
```
$ python -m venv .venv
```

Add your `SECRET_KEY` to the end of the `.venv/bin/activate` file.
```
...
export SECRET_KEY="ThiSIsMyDjanGoSeCreTKey"
```

Activate your virtual environment
```
$ source .venv/bin/activate
```

Install dependencies via pip
```
$ pip install -r requirements.txt
```

### 2. Migrations
Django can create migrations for you. Simply run these commands to create migrations and migrate:
```
$ python manage.py makemigrations shortener
$ python manage.py migrate
```

### 3. Run Server
Run this command to start development server on your computer:
```
$ python manage.py runserver
```
You may access the server at http://localhost:8000/ by default.

<br>

## TODO:
- Add AJAX to front end
- Make responsive
- Url previews and Twitter summary cards support
- Improve analytics

<br>

## Support
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/S6S76FXRP)
