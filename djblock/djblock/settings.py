"""
Django settings for djblock project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ys5&o933n-pip73q)z%fktr!66_u$wv=8!7lzosodg=_h#(mgt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition
SYSTEM_APPS = [
    # system apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # third party apps
    'debug_toolbar',
    'rest_framework',
    'corsheaders',
]

LOCAL_APPS = [
    # local apps
    'polls.apps.PollsConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'community.apps.CommunityConfig',
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djblock.middleware.MediaUrlsAuthMiddleware',
    'accounts.middleware.LoginRequiredMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'djblock.urls'

# =====================================================================
# Django Templates Settings
# =====================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.normpath(os.path.join(BASE_DIR, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# =====================================================================

WSGI_APPLICATION = 'djblock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': get_secret('DATABASE_NAME'),
#         'USER': get_secret('DATABASE_USER'),
#         'PASSWORD': get_secret('DATABASE_PASSWORD'),
#         'HOST': get_secret('DATABASE_HOST'),
#         'PORT': get_secret('DATABASE_PORT'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ),
}

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 30, # (30 seconds after token expired)
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),  # (5 minutes)
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUTH_COOKIE': None,
}

# =====================================================================
# Django CORS headers Configuration need to install and enable
# =====================================================================

# CORS_PREFLIGHT_MAX_AGE = 86400  # Defaults to 86400 (one day).

# CORS_ALLOW_METHODS = (
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# )

# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )

# CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?insmartworld\.com$', )
# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000',
#     'localhost:8080',
#     'localhost:4200',
# )

# CORS_MODEL = 'datacenter.CorsHeadersModel'
# =====================================================================

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)

# =====================================================================
# File Manager
# =====================================================================
# to store files temporary path
FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

# =====================================================================
# Login - Logout - Login Exempts & Auth URLs
# =====================================================================
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
LOGIN_EXEMPT_URLS = (
    r'^$', # Used to load main Angular Page
    r'^api/*',
    r'^login/*',
    r'^logout/*',
    r'^signup/*',
    # r'^accounts/*',
    # r'^media/*',
    r'^api/get-auth-token/$',
    # SERVER HELTH CHECK - GET REQUEST
    r'^server_health/$',
)
# =====================================================================

# =====================================================================
# LOGGING Settings
# =====================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s|%(levelname)s|%(name)s:%(lineno)s|%(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'djblocklogformat': {
            'format': "%(asctime)s|%(levelname)s|%(name)s:%(lineno)s|ACTION: %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/djblock.log',
            'maxBytes': 1024*1024*5,
            'formatter': 'djblocklogformat',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'formatter': 'verbose'
        }
    }
}
# ====================================================================

# ====================================================================
# DEBUG TOOLBAR
# ====================================================================
INTERNAL_IPS = [
    '127.0.0.1'
]
DEBUG_TOOLBAR_CONFIG = {
    'ROOT_TAG_EXTRA_ATTRS': 'ng-non-bindable'
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
# ====================================================================
