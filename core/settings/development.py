from .base import *  # noqa: F403

DEBUG = True

DB = DATABASES["default"]  # noqa: F405

CORS_ALLOW_ALL_ORIGINS = True

# Email - Override to use console backend in development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Swagger settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
