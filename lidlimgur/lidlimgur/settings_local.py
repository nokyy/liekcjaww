SECRET_KEY = 'django-insecure-rguci&2ud80o6g3%^0g%!s4m5&ly4(&_*80yygpx$t*%y4d0j0'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '',
    }
}