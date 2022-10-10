from pathlib import Path
import pymysql
import datetime

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!=a-%q&t(2w1g^)jx0&difxrf7ncckf4^tv=dxb3uf127@4zx2"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "user.apps.UserConfig",
    "memo.apps.MemoConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "djoser",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "pathy",
        "USER": "pathy",
        "PASSWORD": "panda5656",
        "HOST": "db",
        "PORT": "3306",
        # 'OPTIONS': {
        #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        #         },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "/static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

CORS_ALLOW_CREDENTIALS = True

STATIC_URL = "static/"
STATIC_ROOT = "/static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSLES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = "user.MyUser"

DJOSER = {
    # メールアドレスログイン
    "LOGIN_FIELD": "email",
    # アカウント本登録
    "SEND_ACTIVATION_EMAIL": True,
    # アカウント本登録完了メール
    "SEND_CONFIRMATION_EMAIL": True,
    # パスワード変更完了メール
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # メール変更完了メール
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    # 登録時パスワード確認必須
    "USER_CREATE_PASSWORD_RETYPE": True,
    # メール変更時の確認必須
    "SET_USERNAME_RETYPE": True,
    # パスワード変更時の確認必須
    "SET_PASSWORD_RETYPE": True,
    # パスワードリセットURL
    "PASSWORD_RESET_CONFIRM_URL": "api/auth/users/reset_password_confirm/{uid}/{token}",
    # メールアドレスリセットURL
    "USERNAME_RESET_CONFIRM_URL": "api/auth/users/reset_email_confirm/{uid}/{token}",
    # アカウント登録URL
    "ACTIVATION_URL": "localhost:8000/api/auth/users/activation/{uid}/{token}",
    "SERIALIZERS": {
        #'user_create': 'user.serializers.MyUserCreateSerializer',
    },
    # メール文面
    "EMAIL": {
        # アカウント本登録
        "activation": "user.email.ActivationEmail",
        # アカウント本登録完了
        "confirmation": "user.email.ConfirmationEmail",
        # パスワードリセット
        "password_reset": "user.email.PasswordResetEmail",
        # パスワードリセット完了
        "password_changed_confirmation": "user.email.PasswordChangedConfirmationEmail",
        # メールアドレスリセット完了
        "username_changed_confirmation": "user.email.EmailChangedConfirmationEmail",
        # メールアドレスリセット
        "username_reset": "user.email.EmailResetEmail",
    },
}

# メール関連
# ローカル確認
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 本番
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# SMTPサーバーアドレス
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
# 配信元メール
EMAIL_HOST_USER = "ここに配信元メール入れる"
# ここにパスワード
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'xxx@gmail.com'

# 本番ではこんな感じで環境変数に書いたの取る
# EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
# EMAIL_PORT = os.environ.get('EMAIL_PORT', '587')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'administrator')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password')
