from .base import *

DEBUG = True

INTERNAL_IPS = ('127.0.0.1', )

# Example Gmail settings if you need to send email from a local Django dev
# site. Uncomment the following and change the username and password to
# whatever they are for your Gmail account. Make sure don't use Gmail for
# sending email on a production website.
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'username@gmail.com'
# EMAIL_HOST_PASSWORD = 'xxxxxxxx'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

SECRET_KEY = '<change this before going to production>'

ADMINS = (
    ('Your Name', 'username@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',            # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/config/dev.db' % BASE_DIR,  # Or path to database file if using sqlite3.
        'USER': '',                                        # Not used with sqlite3.
    }
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INSTALLED_APPS += (
    'debug_toolbar',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
