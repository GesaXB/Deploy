from pathlib import Path
import dj_database_url
import environ
import os

# Inisialisasi django-environ
env = environ.Env(
    DEBUG=(bool, False)  # Default DEBUG adalah False
)
environ.Env.read_env()  # Membaca file .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')  # Mengambil SECRET_KEY dari file .env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')  # Ambil nilai DEBUG dari file .env

# Allow Railway and custom domains
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

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
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Untuk file statis di production
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
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin configuration (unchanged)
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
