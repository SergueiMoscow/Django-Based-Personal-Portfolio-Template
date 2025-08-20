from pathlib import Path
from environs import Env

# === BASE DIRECTORY ===
BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()
env.read_env(str(BASE_DIR / '.env'))

# === SECURITY SETTINGS ===
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.str('DEBUG', 'false') == 'true'
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# === APPLICATIONS ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')
CSRF_TRUSTED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

# === URL CONFIG ===
ROOT_URLCONF = 'portfolio_site.urls'

# === TEMPLATES ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'portfolio' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.context_processors.portfolio_config',
            ],
        },
    },
]

# === WSGI ===
WSGI_APPLICATION = 'portfolio_site.wsgi.application'

# === DATABASE ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / env.str('DB_FILE', 'db.sqlite3'),
    }
}

# === PASSWORD VALIDATION ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === LOCALIZATION ===
LANGUAGE_CODE = env.str('LANGUAGE_CODE')
TIME_ZONE = env.str('TIME_ZONE')
USE_I18N = True
USE_TZ = True

# === STATIC FILES ===
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'portfolio' / 'static'  # ✅ This expects css/js/images in portfolio/static/portfolio/
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collectstatic in production

# === MEDIA FILES (optional) ===
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# === DEFAULT FIELD TYPE ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_FAILURE_VIEW = 'portfolio.views.csrf_failure'
