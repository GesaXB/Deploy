"""
Django settings for myportofolio project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qkd**r53(m+9&!pca^czxs0ab02@qrm)q!=21of%8bzyqvq!v9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'portofolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myportofolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'myportofolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://postgres:qaaPOxfFUJwMBGHdKWJNpFZnnkMIypiZ@junction.proxy.rlwy.net:24372/railway",
        conn_max_age=600,
        ssl_require=True,
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Path ke folder `static` di proyek
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Lokasi file statis yang dikumpulkan (untuk produksi)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICSTORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    'https://gesaportofolioo.up.railway.app',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

JAZZMIN_SETTINGS = {
    # General settings
    "site_title": "Gesa Portofolio Admin",
    "site_header": "Portofolio Gesa",
    "site_brand": "Gesa Portofolio",
    "welcome_sign": "Welcome to the Dashboard Admin Portofolio",

    # Menampilkan tautan untuk dokumentasi atau referensi
    "topmenu_links": [
        {"name": "Home", "url": "/", "new_window": True},
        {"name": "GitHub Repo", "url": "https://github.com", "new_window": True},
        {"app": "auth"},  # Tautan otomatis ke aplikasi Django bawaan
    ],

    # Custom icons for apps/models
       "icons": {
        "portofolio.Skill": "fas fa-lightbulb",           # Ikon untuk Skill
        "portofolio.Project": "fas fa-project-diagram",  # Ikon untuk Project
        "portofolio.ContactMessage": "fas fa-envelope",  # Ikon untuk Contact Message
        "portofolio.CV": "fas fa-file-pdf",              # Ikon untuk CV
        "auth.User": "fas fa-user",                     # User bawaan Django
        "auth.Group": "fas fa-users",   
    },

    # Sidebar customization
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],  # Apps yang ingin disembunyikan
    "hide_models": [],  # Model yang ingin disembunyikan
    "order_with_respect_to": ["auth", "portfolio"],  # Urutan app di sidebar

    # UI Tweaks
    "default_icon_parents": "fas fa-chevron-circle-down",  # Ikon default untuk parent item
    "default_icon_children": "fas fa-circle",  # Ikon default untuk child item
    "related_modal_active": True,  # Memungkinkan penggunaan modal untuk relasi
    "custom_css": None,  # Tambahkan path CSS custom jika ingin styling tambahan
    "custom_js": None,  # Tambahkan path JS custom jika diperlukan

    # Footer
    "site_footer": "© 2024 Gesa Portofolio. All rights reserved.",
    "copyright": "Portofolio Gesa",

    # Change view customization
    "changeform_format": "collapsible",  # Gunakan form collapsible di halaman change view
    "changeform_format_overrides": {
        "auth.user": "horizontal_tabs",  # Tab horizontal untuk model user
    },
    "custom_css": "css/admin.css",  #
}

# Folder tempat file media akan disimpan
MEDIA_URL = '/media/'  # URL untuk mengakses file media di browser

# Folder fisik tempat file media disimpan
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Folder media berada di direktori proyek
