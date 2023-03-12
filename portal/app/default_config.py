
import datetime
import os

# Encrypt cookies, generate a random cryotographically-secure string
SECRET_KEY = os.urandom(512)

# Session cookies will only be valid for 30 minutes of inactivity
PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# Flask-SQLAlchemy default options
# Some database management systems break connection after some time of inactivity (e.g. MySQL)
# Refresh the connection frequently to circumvent this.
SQLALCHEMY_ENGINE_OPTIONS = { "pool_recycle": 3600 }

# Default data base is sqlite, this is overriden in production
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
