"""
Django settings for ecomstore project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import logging








BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')whe@(4)48$s!#s9ylqm#r^+-#w6q7)6iotg9+8o6exxm_r)zc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECURE_SSL_REDIRECT = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


 
 # if DEBUG:
 #     AALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = ['booksandbooks.herokuapp.com'] 





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',   
    #flat pages
    'django.contrib.flatpages',
    'django.contrib.sites',
    'crispy_forms',
    #added apps
    'catalog',
    'utils',
    'cart',
    'checkout',
    'stripe',
    'accounts',
    'search', 
    'stats', 
    'tagging',
    'marketing',
    'caching',
    'contact', 

] 


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', 
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'SSLMiddleware.SSLRedirect', #not working
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]


ROOT_URLCONF = 'ecomstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.ecomstore',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomstore.wsgi.application' 


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {   

    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'ecomstore',
    #     'USER': 'username',
    #     'PASSWORD': 'password',
    #     'HOST': 'localhost',
    #     'PORT':'3306',
    # },

    # 'postgres': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd48v48nf5ga9kv', 
        'USER': 'vwbtxoucyhxhvi', 
        'PASSWORD': 'ad6ca4c07bb7856a6a2736957f54d253adafaef3619db78122120983dc70e4b7',
        'HOST': 'ec2-23-23-220-163.compute-1.amazonaws.com',
        'PORT': '5432',
    }

}


# Update database configuration with $DATABASE_URL.
if DEBUG == False:
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',

    }
} 
 
 

 



# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




SITE_ID = 1 


PREPEND_WWW = False #True return 301 status code. (False in database) 

CRISPY_TEMPLATE_PACK = 'bootstrap3'





#static files

MEDIA_URL = '/media/' 

STATIC_URL = '/static/'


       
if DEBUG:

    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static') 

    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')    

    STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), ]  



 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'media')
 
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), ] 


#Simplified static file serving. 
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage' 





SITE_NAME = 'book Store' 
META_KEYWORDS = 'books, computer science books, unix, technology, python, django'
META_DESCRIPTION = 'Technology books reviews and for sale' 



 

#---stripe stuff---

#test keys
STRIPE_PUBLISHABLE_KEY = 'pk_test_dgcBsrcAnRwS4tVhNf9x1iCZ'
STRIPE_SECRET_KEY = 'sk_test_WLxYShx8DyIsJkDKDAjQlpFU'


 
    


LOGIN_REDIRECT_URL = '/accounts/my_account/' 
ACCOUNT_LOGOUT_REDIRECT_URL = '/'


#pagination
PRODUCTS_PER_PAGE = 12

#stats
PRODUCTS_PER_ROW = 4 


#cart
SESSION_AGE_DAYS = 90
SESSION_COOKIE_AGE = 60 * 60 * 24 * SESSION_AGE_DAYS


#seconds to keep items in cache
CACHE_TIMEOUT = 60 * 60



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'erickssen@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '587'
EMAIL_USE_TLS = True



























