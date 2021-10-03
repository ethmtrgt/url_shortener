# Simple Url Shortener

![img](https://img.shields.io/github/issues/ethmtrgt/url_shortener)
![img](https://img.shields.io/github/last-commit/ethmtrgt/url_shortener)
![GitHub Repo stars](https://img.shields.io/github/stars/ethmtrgt/url_shortener?style=social)

<br>
<br>

## HOW TO RUN?
### 1. Create Virtual Environment
First create a virtual environment by running this command.
```
$ python -m venv .venv
```

Add your `SECRET_KEY` to the end of the `.venv/bin/activate` file.
```
...
export SECRET_KEY="ThiSIsMyDjanGoSeCreTKey"
```

### 2. Create Migrations
Django can create migrations for you. Simply run this command to create migrations:
```
$ python manage.py makemigrations shortener
$ python manage.py migrate
```

### 3. Run Server
Run this command to start development server on your computer. You may access the server at http://127.0.0.1:8000/ by default.

<br>
<br>

## TODO:
- Add AJAX to front end
- Make responsive
- Url previews and Twitter summary cards support
- Improve analytics
