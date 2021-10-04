# Contributing to Simple Url Shortener

If you would like to contribute to the project, you can do so through [GitHub by forking the repository and sending a pull request.](#contribution-steps)
When submitting code, please make every effort to follow existing conventions and style in order to keep the code as readable as possible. 

Please note we have a [code of conduct](https://github.com/ethmtrgt/url_shortener/blob/main/CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

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
<br>

## Reporting issues & features requests
If you notice any bugs in the project, see some code that can be improved, or have features you would like to be added, please create a bug report or a feature request!

If you want to open a PR that fixes a bug or adds a feature, then it is definitely appreciated if an issue has been created before-hand so it can be discussed first.

## Working on issues

Please feel free to take on any issue that's currently open. Feel free to resolve any issue that you would enjoy working on even if it happens to be a low priority.

## Submitting a PR
- For every PR there should be an accompanying [issue](https://github.com/ethmtrgt/url_shortener/issues) which the PR solves
- The PR itself should only contain code which is the solution for the given issue
- If you are a first time contributor check if there is a [good first issue](https://github.com/ethmtrgt/url_shortener/labels/good%20first%20issue) for you

## Contribution steps

1. Fork this repository to your own repositiry. 
2. Clone the forked repositiry to your local machine.
3. Create your feature branch: `git checkout -b my-new-feature`
4. make changes to the project.
5. Commit your changes: `git commit -m 'Add some feature'`
6. Push to the branch: `git push origin my-new-feature`
7. Submit a pull request :D


## Financial contributions
We also welcome financial contributions. It helps us to grow better and faster.

## License

By contributing your code, you agree to license your contribution under the terms of the [MIT](https://github.com/ethmtrgt/url_shortener/blob/master/LICENSE) license.
All files are released with the MIT license.