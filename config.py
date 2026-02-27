import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # -------------------------
    # Core
    # -------------------------
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
    DEBUG = False
    TESTING = False

    # -------------------------
    # Database
    # -------------------------
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -------------------------
    # Session / CSRF
    # -------------------------
    WTF_CSRF_ENABLED = True

    # -------------------------
    # Mail
    # NOTE: TLS (port 587) and SSL (port 465) are mutually exclusive.
    # Default is TLS. Switch MAIL_USE_TLS=false + MAIL_USE_SSL=true for port 465.
    # -------------------------
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() in ["true", "on", "1"]
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "false").lower() in ["true", "on", "1"]
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", "noreply@example.com")

    # -------------------------
    # Celery
    # -------------------------
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

    # -------------------------
    # JWT
    # -------------------------
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "change-me-jwt-secret")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 86400))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES", 2592000))

    # -------------------------
    # Cache
    # -------------------------
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "RedisCache")
    CACHE_REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/1")

    # -------------------------
    # Rate Limiting
    # -------------------------
    RATELIMIT_STORAGE_URI = os.environ.get("REDIS_URL", "redis://localhost:6379/2")

    # -------------------------
    # Flask-Admin
    # -------------------------
    FLASK_ADMIN_SWATCH = os.environ.get("FLASK_ADMIN_SWATCH", "cerulean")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}