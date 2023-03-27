# Structure

```
myapp/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── post.py
│   │   ├── user.py
│   │   └── role.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── post.py
│   │   ├── user.py
│   │   └── admin.py
│   ├── scripts/
│   │   ├── db_create.py
│   │   ├── db_migrate.py
│   │   └── db_upgrade.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── send_email.py
│   ├── templates/
│   ├── static/
│   └── extensions/
│       ├── __init__.py
│       ├── celery.py
│       ├── db.py
│       ├── login_manager.py
│       ├── admin.py
│       ├── mail.py
│       ├── security.py
│       ├── jwt.py
│       └── api.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_post.py
│   └── test_user.py
├── migrations/
│   └── versions/
│       ├── <migration file 1>.py
│       └── <migration file 2>.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.py
└── .env


```

Python3 Version - 3.10.6

## Virtual Environment (Optional)

    python3 -m venv venv        #for windows replace python3 => python
    source venv/bin/activate    #for windows write "venv/Scripts/activate"

## Installation

    pip install -r requirements.txt

## Run Application On Ubuntu Terminal

    $ export FLASK_APP=manage.py
    $ export FLASK_DEBUG=1  (Remember FLASK_ENV is depricated)
    $ flask run

## Run Application On Windows Powershell

    -> $env:FLASK_APP="app"
    -> $env:FLASK_DEBUG=1
    -> flask run

## Run Application On Windows CMD

    -> set FLASK_APP=app
    -> set FLASK_DEBUG=1
    -> flask run

      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Links

- Flask: https://flask.palletsprojects.com/en/2.2.x/
- Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
- Flask-BluePrint: https://flask.palletsprojects.com/en/2.2.x/blueprints/
- Flask-Mail: https://pythonhosted.org/Flask-Mail/
- Flask-Script: https://flask-script.readthedocs.io/en/latest/
- Celery: https://flask.palletsprojects.com/en/2.2.x/patterns/celery/
- Flask-JWT-Extended: https://flask-jwt-extended.readthedocs.io/en/stable/
- Flask-Admin: https://flask-admin.readthedocs.io/en/latest/
- Flask-Babel: https://python-babel.github.io/flask-babel/
- Flask-RESTful: https://flask-restful.readthedocs.io/en/latest/
- pytest: https://flask.palletsprojects.com/en/2.2.x/testing/
- autopep8: https://pypi.org/project/autopep8/
- Flask-Security: https://flask-security.readthedocs.io/en/3.0.0/
- UUID: Default
- Fakers: https://faker.readthedocs.io/en/master/
  <!-- -   Flask-Login: https://flask-login.readthedocs.io/en/latest/ -->
  <!-- -   Flask-Paranoid: https://flask-paranoid.readthedocs.io/en/latest/ -->
  <!-- -   Flask-Uploads: https://flask-uploads.readthedocs.io/en/latest/ -->

`Installation Command`

1. pip install Flask Flask-SQLAlchemy Flask-Script autopep8 flask-blueprint Flask-Mail celery flask-jwt-extended Flask-Admin flask-babel pytest flask-restful psycopg2-binary Flask-Migrate Flask-Security python-dotenv

 <!-- Flask-Login  Flask-Paranoid Faker-->

## Celery

celery -A app.tasks.celery.celery worker --loglevel=info
