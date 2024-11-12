# Messenger

## Github

###### 📁 Git Clone Project

```cmd
git clone https://github.com/LearnCodingEasy/Messenger.git
```

###### 📝 Create File Gitignore

```
.gitignore
```

###### 🖊️ Write Inside File

```
node_modules/
```

###### 📋 Review changes and formulate change action

###### 📋 مراجعة التغييرات وصياغة إجراء التغيير

```cmd
git status
```

###### 📂 Add all new and changed files to the Staging Area.

###### 📂 أضف كل الملفات الجديدة والمغير إلى منطقة التدريج.

```
git add *
```

###### 💾 This command sends the file from the Staging Area to the Local Repo.

###### 💾 يرسل هذا الأمر الملف من منطقة التدريج إلى الريبو المحلي.

```cmd
git commit -m "Commit Explain Code"
```

###### 🌐 This command sends files from (Local Repo) to (Remote Repo).

###### 🌐 يرسل هذا الأمر ملفات من (repo المحلي) إلى (ريبو عن بعد).

```cmd
git push origin main
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## LICENSE

Create File 📝 [ LICENSE ]

```text
LICENSE
```

```text
MIT License
Copyright (c) 2024 Hossam Rashad
📍 +0201091642528
📍 +0201101853042
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vite Press

###### 🖥️ Create Vuepress

```cmd
npm init vuepress messenger_vuepress
```

###### 🖥️ Command Path

```cmd
cd messenger_vuepress
```

###### 🖥️ Install Sass

```cmd
npm install -D sass-embedded
```

###### 📝 Create File [ index.md ] Inside Docs

```
index.md
```

###### 🖥️ Run Vue Press

```cmd
npm run docs:dev
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Django

### 🖥️ Virtual Environment

###### 🖥️ Create Virtual Environment 🐍

```cmd
python -m venv messenger_virtual_environment
```

###### 🚀 Activate Virtual Environment 🔋

```cmd
messenger_virtual_environment\Scripts\activate
```

### 🔧 Install Django

###### 🔧 Install Django 🦄

```cmd
pip install django
```

###### 🔧 Django Version 🦄

```cmd
python -m django --version
```

### 🛠️ Django Libraries

###### 🛠️ Install Django Libraries 📚

1 - 🌐 Django Rest Framework

```cmd
pip install djangorestframework
```

2 - 🔒 Django Rest Framework Simplejwt 🛡️

```cmd
pip install djangorestframework-simplejwt
```

3 - 🌍 Django Cors Headers 🔗

```cmd
pip install django-cors-headers
```

4 - 🖼️ pillow 📷

```
pip install pillow
```

### 📂 Create Django Project

```cmd
django-admin startproject messenger_django
```

### 👤 Create Django App Account

```cmd
cd messenger_django
```

```cmd
python manage.py startapp account
```

### ⚙️ Settings

#### ⚙️ Page Settings [ settings.py ] 📝

```python
# Page [messenger/messenger_django/messenger_django/settings.py]

from datetime import timedelta

# The address of the site that points to the local server.
WEBSITE_URL = "http://127.0.0.1:8000"

# Define the default user model used in the application.
AUTH_USER_MODEL = "account.User"

# SIMPLE_JWT library settings to specify the validity period of tokens
# Access Token Validity (30 days)
# Refresh Token Validity (180 days)
# Disable Auto Refresh Tokens
SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
  "ROTATE_REFRESH_TOKENS": False,
}

# Django REST Framework settings for identity and permissions verification
# Use JWT for identity verification
# Allow only authenticated users
REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
      "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
  "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# Allow CORS requests from specific addresses
# Allow requests from this origin
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

# Allow CSRF requests from specific addresses
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    # Libraries [ Django Cors Headers ]
    "corsheaders.middleware.CorsMiddleware",
    # ...
]
# Access path for static files (such as CSS and JavaScript files)
STATIC_URL = "static/"
# Access path for media files (such as images and files uploaded by users)
MEDIA_URL = "media/"
# Specify a "media" folder in the project to store uploaded media files
MEDIA_ROOT = BASE_DIR / "media"
```
