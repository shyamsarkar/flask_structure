Structure
=========

```
myapp/
├── app/
│   ├── __init__.py              # create_app(), blueprint + extensions init
│
│   ├── extensions/              # third-party integrations (NO app logic)
│   │   ├── __init__.py
│   │   ├── db.py                # SQLAlchemy()
│   │   ├── migrate.py           # Flask-Migrate
│   │   ├── login_manager.py     # Flask-Login (ADDED)
│   │   ├── cache.py
│   │   ├── limiter.py
│   │   ├── mail.py
│   │   └── celery.py
│
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py              # timestamps, soft delete (kept)
│   │   ├── user.py              # User + UserMixin
│   │   ├── tenant.py
│   │   └── membership.py
│
│   ├── services/                # business logic (NO Flask imports)
│   │   ├── __init__.py
│   │   ├── auth_service.py      # login/register helpers
│   │   ├── tenant_service.py
│   │   └── membership_service.py
│
│   ├── web/                     # HTML routes (PRIMARY interface)
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── routes.py        # login/logout/register
│   │   └── tenants/
│   │       ├── __init__.py
│   │       └── routes.py
│
│   ├── api/                     # JSON API (OPTIONAL, parallel)
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   └── tenants/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       └── schemas.py
│
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── send_email.py        # Celery task (uses app context)
│
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── tenants/
│   │       └── dashboard.html
│
│   └── static/
│       ├── css/
│       └── js/
│
├── migrations/
│   └── versions/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── web/                     # HTML/login tests
│   ├── api/
│   └── services/
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt
├── .env.sample
├── wsgi.py                      # gunicorn entrypoint
├── config.py
└── README.md
```

Python Version
--------------

```
Python 3.10.6
```
If you use **asdf**, install and set the version like this:

```bash
asdf plugin add python
asdf install python 3.10.6
asdf local python 3.10.6
```

Verify
-------
```
python --version
```

Virtual Environment (Optional)
------------------------------

```bash
python3 -m venv venv          # Windows: python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

Installation
------------

```bash
pip install -r requirements.txt
```

Environment Variables
---------------------

Create a `.env` file:

```env
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379/0
```

Run Application
---------------

```bash
flask --app wsgi run
```

Application runs at:

```
http://127.0.0.1:5000/
```

Database Commands
-----------------

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

Links
-----

- Flask  
  https://flask.palletsprojects.com/

- Flask-SQLAlchemy  
  https://flask-sqlalchemy.palletsprojects.com/

- Flask Blueprints  
  https://flask.palletsprojects.com/en/latest/blueprints/

- Flask-JWT-Extended  
  https://flask-jwt-extended.readthedocs.io/

- Flask-Mail  
  https://pythonhosted.org/Flask-Mail/

- Celery (Flask pattern)  
  https://flask.palletsprojects.com/en/latest/patterns/celery/

- Flask-Admin  
  https://flask-admin.readthedocs.io/

- Flask-Babel  
  https://python-babel.github.io/flask-babel/

- pytest  
  https://docs.pytest.org/

- Faker  
  https://faker.readthedocs.io/

Installation Command
--------------------

```bash
pip install \
Flask \
Flask-SQLAlchemy \
Flask-Migrate \
Flask-JWT-Extended \
Flask-WTF \
Flask-Mail \
Flask-Caching \
Flask-Limiter \
Flask-Admin \
Flask-Babel \
celery \
redis \
python-dotenv \
psycopg2-binary \
pytest \
faker \
black \
ruff \
gunicorn
```

Notes
-----

- Flask-Script is deprecated and not used
- Flask-RESTful is intentionally avoided
- Routes are thin, business logic lives in services
- API and Web layers are clearly separated
- Redis is required for Celery and Flask-Limiter

