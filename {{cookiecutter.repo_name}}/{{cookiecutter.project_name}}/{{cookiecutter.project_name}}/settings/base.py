"""
Django settings for {{ cookiecutter.project_name }} project.
"""

from os import environ, getenv
from os.path import abspath, basename, dirname, join, normpath
from sys import path

########## PATH CONFIGURATION
BASE_DIR = dirname(dirname(__file__) + "../../../")

# Absolute filesystem path to the config directory:

CONFIG_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the project directory:
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Absolute filesystem path to the django repo directory:
DJANGO_ROOT = dirname(PROJECT_ROOT)

# Project name:
PROJECT_NAME = basename(PROJECT_ROOT).capitalize()

# Project folder:
PROJECT_FOLDER = basename(PROJECT_ROOT)

# Project domain:
PROJECT_DOMAIN = '%s.com' % PROJECT_NAME.lower()

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(CONFIG_ROOT)
########## END PATH CONFIGURATION

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

########## DEBUG CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = STAGING = False
########## END DEBUG CONFIGURATION

ADMINS = (
    ("""{{cookiecutter.author_name}}""", '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                       # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = '{{ cookiecutter.timezone }}'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = '{{cookiecutter.languages.strip().split(',')[0]}}'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'assets'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    normpath(join(PROJECT_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (normpath(join(PROJECT_ROOT, 'templates')),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                {% if cookiecutter.cms_package == "django-cms" %}
                'sekizai.context_processors.sekizai',
                {% endif %}
                'django.template.context_processors.static',

                {% if cookiecutter.cms_package == "django-cms" %}
                'cms.context_processors.cms_settings'
                {% endif %}
            ]
        },
    },
]

MIDDLEWARE = (
    {% if cookiecutter.cms_package == "django-cms" %}
    'cms.middleware.utils.ApphookReloadMiddleware',
    {% endif %}
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    {% if cookiecutter.cms_package == "django-cms" %}
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    {% endif %}

    'kn_defaults.logging.middlewares.KnLogging',
)

ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'

INSTALLED_APPS = (
    {% if cookiecutter.cms_package == "django-cms" %}
    # Django CMS admin style
    'djangocms_admin_style',
    {% endif %}

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'kn_defaults.logging',

    {% if cookiecutter.cms_package == "django-cms" %}
    # Django CMS
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    {% endif %}

    {% if cookiecutter.django_filer == "y" or cookiecutter.django_filer == "Y" %}
    # Django filer
    'filer',
    'easy_thumbnails',
    {% endif %}

    'compressor',
    {% if cookiecutter.s3 == "y" or cookiecutter.s3 == "Y" %}
    'storages',
    {% endif %}
)

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

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
KN_LOG_FILE_PATH = join(DJANGO_ROOT, 'logs/log.log')

from kn_defaults.logging.defaults import BASE_LOGGING
BASE_LOGGING['handlers'].update({
    'sentry': {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        'tags': {'custom-tag': 'x'},
    },
})
BASE_LOGGING.update({
    'root': {
        'handlers': ['sentry'],
        'level': 'DEBUG',
    },
})
LOGGING = BASE_LOGGING

KN_LOGGING_URL_PATTERNS = []

LOCALE_PATHS = (normpath(join(PROJECT_ROOT, 'locale')),)

# Dummy gettext function
gettext = lambda s: s

LANGUAGES = [
    {% for language in cookiecutter.languages.strip().split(',') -%}
    ('{{ language|trim }}', gettext('{{ language|trim }}')),
    {% endfor %}
]

{% if cookiecutter.cms_package == "django-cms" %}
# Django CMS configurations
CMS_TEMPLATES = (
    ('single_page.html', gettext('Single page')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [{% for language in cookiecutter.languages.strip().split(',') %}
        {
            'public': True,
            'code': '{{ language|trim }}',
            'hide_untranslated': False,
            'name': gettext('{{ language|trim }}'),
            'redirect_on_fallback': True,
        },
        {% endfor %}

    ],
}

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}
{% endif %}

{% if cookiecutter.django_filer == "y" or cookiecutter.django_filer == "Y" %}
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
{% endif %}

# Analytics
GOOGLE_ANALYTICS = environ.get('GOOGLE_ANALYTICS', '')

CACHE_ENGINES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
    },
    'dummy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CACHES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
    }
}

CACHES['default'] = CACHE_ENGINES[getenv('CACHE', 'dummy')]

########## REDIS QUEUE CONFIGURATION
# https://github.com/ui/django-rq#support-for-django-redis-and-django-redis-cache
RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'redis'
    },
    'high': {
        'USE_REDIS_CACHE': 'redis'
    },
    'low': {
        'USE_REDIS_CACHE': 'redis'
    }
}

RQ_SHOW_ADMIN_LINK = True
########## END REDIS QUEUE CONFIGURATION

RAVEN_CONFIG = {
	"dsn": ""
}