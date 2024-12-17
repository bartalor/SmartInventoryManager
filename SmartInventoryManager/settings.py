import os

BASE_DIR = "/home/bar/my_mount/SmartInventoryManager"
APP_NAME = 'SmartInventoryManager'
SECRET_KEY = "your-secret-key"
DEBUG = True
ALLOWED_HOSTS = []
DEFAULT_DATABASE = os.getenv('DEFAULT_DATABASE', 'main')  # Default to 'main' if not set
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
     "rest_framework",
    APP_NAME,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = f"{APP_NAME}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = f"{APP_NAME}.wsgi.application"

DATABASES = {
    'main':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/bar/data/SmartInventoryManager/db.sqlite3',
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/bar/data/SmartInventoryManager/db.sqlite3_test',
    }
}

DATABASES['default'] = DATABASES[DEFAULT_DATABASE]


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = f"{APP_NAME}.User"