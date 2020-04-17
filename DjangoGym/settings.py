import os
import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'pgt*mbtn_2v0t)21()sk^$)8g@2w*e+n5ac&%h)ivu27qib1cw'


DEBUG = True

ALLOWED_HOSTS = ['*']


CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (

  'http://localhost:4200',
)

APPEND_SLASH = False


JWT_AUTH = {
    # Authorization:Token xxx
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
}


INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
    'SmartGym',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'auditlog',
]


SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'


REST_USE_JWT = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = 'DjangoGym.urls'

MEDIA_URL = '/media/'
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)

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

WSGI_APPLICATION = 'DjangoGym.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



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



LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_ITEMS = [
    {'label': ('Auditoria'), 'app_label': 'auditlog', 'items': [
        {'name': 'logentry', 'label': ('Registro de Auditoria')},
    ]},
    {'app_label': 'auth', 'items': [
        {'name': 'group'},
        {'name': 'user'},
    ]},
    {'app_label': 'SmartGym', 'items': [
        {'name': 'actividad'},
        {'name': 'asistenciaempleado'},
        {'name': 'asistenciasocio'},
        {'name': 'autoridad'},
        {'name': 'consultorio'},
        {'name': 'cuota'},
        {'name': 'ejercicio'},
        {'name': 'empleado'},
        {'name': 'horario'},
        {'name': 'horarioconsultorio'},
        {'name': 'insumo'},
        {'name': 'liquidacion'},
        {'name': 'profesionalxconsultorios'},
        {'name': 'profesional'},
        {'name': 'proveedor'},
        {'name': 'recordatorio'},
        {'name': 'caja'},
        {'name': 'posiblecliente'},
        {'name': 'rutinaxejercicio'},
        {'name': 'rutina'},
        {'name': 'socio'},
        {'name': 'sucursal'},
        {'name': 'turno'},
    ]},
    {'app_label': 'authtoken', 'items': [
        {'name': 'token'},
    ]},
]


