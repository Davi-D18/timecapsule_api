from .base import *  # noqa: F403
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DB = DATABASES["default"]

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],  # Altere para 'console'
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

ALLOWED_HOSTS = ['https://timecapsule-api.onrender.com']

CORS_ALLOWED_ORIGINS = [
    'https://timecapsule-front.vercel.app',
]