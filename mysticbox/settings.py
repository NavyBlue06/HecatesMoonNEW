from pathlib import Path
import os  # Needed for reading env vars later when I add your Stripe keys securely

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ob8^c9a+tc_=df$ch=*)na^)l&)yr9^7sl-rx96$=f@j$o7f39'

DEBUG = True

ALLOWED_HOSTS = []

# --- Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'home',
    'boxes',
    'cart',
    'services',
    'hecatemarket',
    'checkout',  #  Just added for Stripe 
    'crispy_bootstrap4',
    'crispy_forms',  # For better form styling
    'django_countries',  # For country selection in forms
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysticbox.urls'

# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysticbox.wsgi.application'

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static & Media ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Auth ---
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGIN_METHOD = 'username_email'
ACCOUNT_SIGNUP_FIELDS = ["email", "username", "password1", "password2"]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# --- Cart session ---
CART_SESSION_ID = 'cart'

# --- Stripe (placeholders for now, will be securely read later from env or form setup) ---
STRIPE_PUBLIC_KEY = 'your-public-key-here'
STRIPE_SECRET_KEY = 'your-secret-key-here'

# --- Email backend (for later: confirmation emails) ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # change in prod
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

