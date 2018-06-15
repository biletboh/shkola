"""
Django settings for shkola project.
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dylnv!3$)6+1sf#&6w+r8h2sdrt4^wqifmo(fl-njj3dcdii*7'
SECRET_KEY = os.environ.get('SECRET_KEY', 'default')

# Application definition

INSTALLED_APPS = [
    # custom apps
    'blog.apps.BlogConfig',
    'core.apps.CoreConfig',
    'information.apps.InformationConfig',
    'theteachers.apps.TheteachersConfig',

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # external apps
    'easy_thumbnails',
    'tinymce',
    'django_file_form',
    'django_file_form.ajaxuploader',
    'widget_tweaks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shkola.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'shkola.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    }
}

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

LOGIN_REDIRECT_URL = '/blog/update/list/'

# Internationalization

LANGUAGE_CODE = 'uk'

LANGUAGES = (
        ('uk', _('Ukrainian')),
        ('pl', _('Polish'))
        )

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
            os.path.join(BASE_DIR, 'locale'),
            )


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Log to a text file that can be rotated by logrotate
        'logfile': {
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(BASE_DIR, 'website.log')
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

# TinyMCE config
TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = '/static/tiny_mce'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': ('advlist,autolink,autoresize,fullpage,fullscreen,'
                + 'table,paste,searchreplace,wordcount'),
    'theme': "advanced",
    'theme_advanced_resizing': True,
    'theme_advanced_resize_horizontal': True,
    'theme_advanced_buttons1': ('undo,redo,bold,italic,'
                                + 'underline,strikethrough,|,forecolor,'
                                + 'backcolor,|,bullist,numlist,|,justifyleft,'
                                + 'justifycenter,justifyright,justifyfull,|,'
                                + 'outdent,indent,|,link,unlink,|,'
                                + 'blockquote,|,hr,charmap'),
    'width': '100%',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    }
TINYMCE_COMPRESSOR = False

# Thumbnails setup
THUMBNAIL_ALIASES = {
    '': {
        'blog_preview': {'size': (830, 550), 'crop': True},
        'blog': {'size': (1350, 900), 'crop': True},
        'teacher': {'size': (300, 450), 'crop': True},
    },
}
