from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'default')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Security configuration
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
