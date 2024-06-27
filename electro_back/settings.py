"""
Django settings for electro_back project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
# postgresql on render
import dj_database_url


from pathlib import Path
import environ
env = environ.Env()
environ.Env.read_env()
 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("SECRET_KEY")
# ENCRYPT_KEY = env('ENCRYPT_KEY')
DATABASE_URL = "postgresql://postgres:jXkkPmDGsIHTWZMFQNofTfbTbotGbbEb@roundhouse.proxy.rlwy.net:15803/railway"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account',
    'seller',
    'categories',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
]

# my changes new
# AUTH_USER_MODEL = 'account.CustomUser'

# AUTH_USER_MODEL = 'account.CustomUser'

CORS_ORIGIN_WHITELIST = (
    'http://localhost:5173', 'https://electro-mart-eta.vercel.app/','https://electro-mart-backend.up.railway.app/'
)

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
# ]

# CSRF_TRUSTED_ORIGINS = ['https://electro-mart-backend.onrender.com', 'https://*.127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
    'https://electro-mart-backend.onrender.com',
    'https://*.127.0.0.1',
    'http://localhost:5173',
    'https://electro-mart-eta.vercel.app',
    'https://electro-mart-backend.up.railway.app'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://electro-mart-eta.vercel.app',
    'https://electro-mart-backend.up.railway.app'
]

ACCESS_CONTROL_ALLOW_ORIGIN = ['http://localhost:5173', 'https://electro-mart-eta.vercel.app']

CORS_ALLOW_ALL_ORIGINS = True

AUTHENTICATION_BACKENDS = [
    # 'path.to.Emailbackend',
    'account.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend', 
]



# my changes end

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', 
        'rest_framework.authentication.TokenAuthentication', 
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
#    'rest_framework.permissions.IsAuthenticated',
]
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'electro_back.urls'

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

WSGI_APPLICATION = 'electro_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASS"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }

DATABASES = {
    'default': dj_database_url.config(        # Replace this value with your local database's connection string.        
        default=DATABASE_URL, conn_max_age=1000   )}

# DEBUG = env('ENVIRONMENT') == 'development'

# if env('ENVIRONMENT') == 'development':
#     DEBUG = True
# else:
#     DEBUG = False

# if env('ENVIRONMENT') == 'development':
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': env('DB_NAME'),
#             'USER': env('DB_USER'),
#             'PASSWORD': env('DB_PASS'),
#             'HOST': env('DB_HOST'),
#             'PORT': env('DB_PORT'),
#         }
#     }
# else:
#     DATABASES = {
#         'default': dj_database_url.config(
#             default=env('DATABASE_URL')
#         )
#     }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
