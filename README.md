MVT Structure
=========

```
myapp/
├── app/
│   ├── __init__.py              # create_app(), blueprint + extensions init
│   │
│   ├── extensions/              # third-party integrations (NO app logic)
│   │   ├── __init__.py
│   │   ├── db.py                # SQLAlchemy()
│   │   ├── migrate.py           # Flask-Migrate
│   │   ├── login_manager.py     # Flask-Login (ADDED)
│   │   ├── cache.py
│   │   ├── limiter.py
│   │   ├── mail.py
│   │   └── celery.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py              # timestamps, soft delete (kept)
│   │   ├── user.py              # User + UserMixin
│   │   ├── tenant.py
│   │   └── membership.py
│   │
│   ├── services/                # business logic (NO Flask imports)
│   │   ├── __init__.py
│   │   ├── auth_service.py      # login/register helpers
│   │   ├── tenant_service.py
│   │   └── membership_service.py
│   │
│   ├── web/                     # HTML routes (PRIMARY interface)
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── views.py        # login/logout/register
│   │   └── tenants/
│   │       ├── __init__.py
│   │       └── views.py
│   │
│   ├── api/                     # JSON API (OPTIONAL, parallel)
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   └── schemas.py
│   │   └── tenants/
│   │       ├── __init__.py
│   │       ├── views.py
│   │       └── schemas.py
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── send_email.py        # Celery task (uses app context)
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── tenants/
│   │       └── dashboard.html
│   │
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
Python 3.12.12
```
If you use **asdf**, install and set the version like this:

```bash
asdf plugin add python
asdf install python 3.12.12
asdf set python 3.12.12
```

Verify
-------
```
python --version
```

Virtual Environment (Optional)
------------------------------

```bash
python3 -m venv venv          # Try: python -m venv venv
source venv/bin/activate
```

Installation
------------

```bash
pip install -r requirements.txt
```

Environment Variables
---------------------

Copy `.env.sample` and rename it to `.env`


Run Application
---------------
Terminal 1 - Flask Application
```bash
flask --app wsgi:app run --debug
```

Terminal 2 - Celery Background Jobs
```bash
celery -A wsgi.celery worker --loglevel=info
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

Console Command
-----------------

```bash
flask shell
```
before this, verify FLASK_APP=wsgi.py exists in .env


Mail (Development)
------------------
 
In development, emails are caught by [MailHog](https://github.com/mailhog/MailHog) — no real emails are sent.
 
Start MailHog:
 
```bash
docker run --name mailhog -p 1025:1025 -p 8025:8025 mailhog/mailhog
```
 
Add these to your `.env`:
 
```
MAIL_SERVER=localhost
MAIL_PORT=1025
MAIL_USE_TLS=False
MAIL_USE_SSL=False
MAIL_USERNAME=
MAIL_PASSWORD=
```
 
View caught emails at:
 
```
http://localhost:8025
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

Create Root User
----------------

After running migrations, create the first root user via the CLI:

```bash
flask custom create-root-user \
  --email admin@example.com \
  --password 'Password123' \
  --first-name Admin \
  --last-name User \
  --tenant-name Main
```

This command:
- Creates the user and a unique referral code like `MLM0001`
- Creates the tenant if it doesn't exist
- Assigns the user an `admin` membership in that tenant


# Test Network Ecosystem

Here are the mock users currently populated in the system for testing the network tree nesting and commissions.

**Universal Test Password:** `Password123`

| Name | Email | Generation | Sponsored By |
| :--- | :--- | :--- | :--- |
| **Admin Root** | `admin@example.com` | Root | - |
| **Alice Test** | `alice@example.com` | Level 1 | Admin Root |
| **Bob Test** | `bob@example.com` | Level 1 | Admin Root |
| **Hank Test** | `hank@example.com` | Level 1 | Admin Root |
| **Charlie Test** | `charlie@example.com` | Level 2 | Alice Test |
| **Diana Test** | `diana@example.com` | Level 2 | Alice Test |
| **Eve Test** | `eve@example.com` | Level 2 | Alice Test |
| **Frank Test** | `frank@example.com` | Level 2 | Bob Test |
| **Grace Test** | `grace@example.com` | Level 3 | Charlie Test |
| **Ivy Test** | `ivy@example.com` | Level 3 | Charlie Test |

> [!TIP]
> Try logging in as **Alice Test** (`alice@example.com`) to see what a mid-level manager's view of the Tree looks like compared to the Admin's view!
