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

### 🧑 Account Page [ models.py ]

#### 🧑 App [ Account ] Page [ models.py ] 📝

```python
# 📄 صفحة [messenger/messenger_django/account/models.py]
# uuid: يُستخدم لإنشاء معرّفات فريدة عالمياً
# (UUID) التي يمكن استخدامها لتعريف المستخدمين.
import uuid

# settings: لاستيراد إعدادات
# Django الخاصة بالمشروع.
from django.conf import settings

# AbstractBaseUser, PermissionsMixin: لإنشاء نموذج مستخدم مخصص.
# UserManager: لإدارة إنشاء المستخدمين.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# models: لإنشاء نماذج Django.
from django.db import models

# Time
# timezone: للتعامل مع التوقيتات.
from django.utils import timezone
from django.utils.timesince import timesince


# 👥 Dedicated manager to create and manage users
# 👥 مدير مخصص لإنشاء وإدارة المستخدمين
class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        # ✉️ Verify email entry
        # ✉️ تحقق من إدخال البريد الإلكتروني
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 👤 Create a regular user
    # 👤 إنشاء مستخدم عادي
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    # 🛡️ Create an administrative user (super user)
    # 🛡️ إنشاء مستخدم إداري (سوبر يوزر)
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


# 🧑 Custom User Form
# 🧑 نموذج المستخدم المخصص
class User(AbstractBaseUser, PermissionsMixin):
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 📛 User Data Properties خصائص بيانات المستخدم
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    surname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=15, blank=True, null=True)
    # 🖼️ Profile Picture صورة شخصية
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    # 🖼️ Cover Photo صورة الغلاف
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    # ⚙️ User Status  حالة المستخدم
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # 📋 Custom Admin Link ربط المدير المخصص
    objects = CustomUserManager()

    # 👥 Friends and Characteristics of Friendships الأصدقاء وخصائص الصداقات
    friends = models.ManyToManyField("self")
    friends_count = models.IntegerField(default=0)
    people_you_may_know = models.ManyToManyField("self")

    # 📋 Tasks and Their Number المهام وعددها
    task_count = models.IntegerField(default=0)

    # 📅 Join Date & Last Login تاريخ الانضمام وآخر تسجيل دخول و حالة الاتصال
    # Automatic
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_online = models.BooleanField(default=False)

    # 🔒 إعدادات تسجيل الدخول: البريد الإلكتروني كمحدد رئيسي لتسجيل الدخول
    # يحدد الحقل الذي سيتم استخدامه لتسجيل الدخول. في هذه الحالة، هو email.
    USERNAME_FIELD = "email"
    # يحدد الحقل الذي يتم استخدامه كالبريد الإلكتروني الرئيسي للمستخدم. في هذه الحالة، هو email.
    EMAIL_FIELD = "email"
    # 📝 لا توجد حقول إضافية مطلوبة بجانب البريد الإلكتروني وكلمة المرور عند إنشاء مستخدم جديد عبر الأوامر الإدارية.
    REQUIRED_FIELDS = []

    # 🖼️ Function to get cover image link With default link if none exists
    # 🖼️ دالة للحصول على رابط صورة الغلاف مع رابط افتراضي إذا لم تكن موجودة
    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return "https://picsum.photos/200/200"

    def get_cover(self):
        if self.cover:
            return settings.WEBSITE_URL + self.cover.url
        else:
            return "https://picsum.photos/200/200"

    def date_joined_formatted(self):
        return timesince(self.date_joined)


# 📬 Friend Request Form نموذج طلب الصداقة
class FriendshipRequest(models.Model):
    # 📝 Friend request cases  حالات طلب الصداقة
    SENT = "sent"
    NOT_SENT = "not sent"
    ACCEPTED = "accepted"
    WAITING = "waiting"
    REJECTED = "rejected"
    CANCEL = "cancel"

    STATUS_CHOICES = (
        (SENT, "Sent"),
        (NOT_SENT, "Not Sent"),
        (ACCEPTED, "Accepted"),
        (WAITING, "Waiting"),
        (REJECTED, "Rejected"),
        (CANCEL, "Cancel"),
    )
    # 🔑 Friend Request UUID Essential Field حقل أساسي UUID لطلب الصداقة
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 🧑 User receiving the request  المستخدم المستلم للطلب
    created_for = models.ForeignKey(
        User, related_name="received_friendshiprequests", on_delete=models.CASCADE
    )
    # 📅 Creation date تاريخ الإنشاء
    created_at = models.DateTimeField(auto_now_add=True)
    # 🧑 The user who sent the request  المستخدم المرسل للطلب
    created_by = models.ForeignKey(
        User, related_name="created_friendshiprequests", on_delete=models.CASCADE
    )
    # 📝 Order Status  حالة الطلب
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOT_SENT)
```

### 🆕 Makemigrations

###### 🛠️ Modifications To Models File | تعديلات على ملف النماذج

```cmd
python manage.py makemigrations
```

### 🛠️ Makemigrations

###### 🛠️ Migrate To The Database |الانتقال إلى قاعدة البيانات

```cmd
python manage.py migrate
```

### 🧑 Account Page [ admin.py ]

#### 🧑 App [ Account ] Page [ admin.py ] 📝

```python
from django.contrib import admin
from .models import User
admin.site.register(User)
```

### 🧑 Account Page [ serializers.py ]

#### 🧑 App [ Account ] Page [ serializers.py ] 📝

```
serializers.py
```

```python
#  📝 Page [ messenger/messenger_django/account/serializers.py ]

# استيراد الاطار لتحويل البيانات
from rest_framework import serializers

# استيراد نموذج البيانات المراد تحويلة
from .models import User, FriendshipRequest

# from django.utils import timezone


# 🧑 سيريلايزر لمستخدم
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # النموذج المرتبط بالسيريلايزر
        # النموذج المراد استخدامه
        model = User
        # الحقول المطلوبة
        # 🔍 تستخدم لتحديد الحقول المضمنة في البيانات المُسترجعة أو المرسلة عبر المسلسل.
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "get_avatar",
            "get_cover",
            # Friends
            "friends_count",
            # Tasks
            "task_count",
            # Data & Time
            "date_joined",
            "date_joined_formatted",
            "last_login",
            "is_online",
        )


class FriendshipRequestSerializer(serializers.ModelSerializer):
    # 👤 Sender information using UserSerializer (read-only)
    # 👤 معلومات المرسل باستخدام المستخدمين (القراءة فقط)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendshipRequest
        # 🆔 Request ID and sender data
        # 🆔 طلب معرف وبيانات المرسل
        fields = (
            "id",
            "created_by",
            "status"
        )
```

### 🧑 Account Page [ forms.py ]

#### 🧑 App [ Account ] Page [ forms.py ] 📝

```
forms.py
```

```python
# 📄 ملف [ messenger/messenger_django/account/forms.py ]

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# 📝 نموذج التسجيل
class SignupForm(UserCreationForm):
    # 🔧 إعدادات النموذج: تحديد الحقول المطلوبة
    class Meta:
        model = User
        fields = (
            # 🧑 الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🔑 كلمة المرور
            "password1",
            # 🔑 تأكيد كلمة المرور
            "password2",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            # 🧑 User's name الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 User's email البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🖼️ User's profile picture صورة ملف تعريف المستخدم
            "avatar",
            # 🖼️ User's Cover picture صورة ملف غلااف المستخدم
            "cover",
        )

```

### 🧑 Account Page [ api.py ]

#### 🧑 App [ Account ] Page [ api.py ] 📝

```python
api.py
```

```python
# 📄 ملف [ messenger/messenger_django/account/api.py ]

# 🌐 API for User Signup and Profile Info Retrieval
# 🌐 API لتسجيل المستخدم واسترجاع معلومات الحساب

# Django إستيراد إعدادات المشروع في
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm, ProfileForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User, FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer, FriendshipRequestSerializer


# 📝 Signup API Endpoint
# 📝 واجهة برمجية للتسجيل
@api_view(["POST"])
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def signup(request):
    data = request.data
    message = "success"

    # 🧾 Initialize signup form with request data
    # 🧾 تهيئة نموذج التسجيل باستخدام بيانات الطلب
    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    # ✅ Check if form is valid
    # ✅ التحقق من صحة النموذج
    if form.is_valid():
        # 🛠️ Save the new user
        # 🛠️ حفظ المستخدم الجديد
        user = form.save()
        # 🔓 Activate the account
        # 🔓 تأكيد الحساب مباشرة
        user.is_active = True
        user.save()

        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # ❌ If errors exist, return them
        # ❌ إذا كان هناك أخطاء
        message = form.errors.as_json()
    # 🔍 Print errors for debugging
    # 🔍 طباعة الأخطاء لأغراض التصحيح
    print(message)
    return JsonResponse({"message": message}, safe=False)


# 👤 User Info API Endpoint
# JSON إرجاع بيانات المستخدم الحالي كاستجابة
# 👤 واجهة برمجية لاسترجاع معلومات المستخدم
@api_view(["GET"])
def me(request):
    if request.user.is_authenticated:
        user_serializer = UserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)
    return JsonResponse({"error": "User not authenticated"}, status=401)


# Profile
@api_view(["GET"])
def profile(request, id):
    # (primary key) استرجاع معلومات المستخدم بناءً على معرفه الفريد
    user = User.objects.get(pk=id)
    # print("Profile User By Id 👉️", user)
    # (primary key)
    # تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص
    user_serializer = UserSerializer(user)
    # print("Profile User By Id 👍", user_serializer)

    #
    can_send_friendship_request = True

    if request.user in user.friends.all():
        can_send_friendship_request = False

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    if check1 or check2:
        can_send_friendship_request = False

    # JSON إرجاع البيانات كاستجابة
    return JsonResponse(
        {
            "user": user_serializer.data,
            "can_send_friendship_request": can_send_friendship_request,
        },
        safe=False,
    )


@api_view(["POST"])
def editprofile(request):
    # 👤 Get current user and new email data
    # 👤 احصل على بيانات بريد إلكتروني حالية وبيانات بريد إلكتروني جديدة
    user = request.user
    email = request.data.get("email")

    # 📧 Check if email is already in use by another user
    # 📧 تحقق مما إذا كان البريد الإلكتروني قيد الاستخدام بالفعل من قبل مستخدم آخر
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({"message": "email already exists"})
    else:
        # 📝 Initialize profile form with request data and files
        # 📝 تهيئة نموذج الملف الشخصي مع بيانات الطلب والملفات
        form = ProfileForm(request.POST, request.FILES, instance=user)

        # ✅ Validate and save profile if valid
        # ✅ التحقق من صحة وحفظ الملف الشخصي إذا كان صالحًا
        if form.is_valid():
            form.save()

        # 🔄 Serialize updated user data
        # 🔄 قم بتسلسل بيانات المستخدم المحدثة
        serializer = UserSerializer(user)
        return JsonResponse({"message": "information updated", "user": serializer.data})


@api_view(["POST"])
def editpassword(request):
    # 🔒 Initialize password change form with request data
    # 🔒 تهيئة نموذج تغيير كلمة المرور مع بيانات الطلب
    user = request.user
    form = PasswordChangeForm(data=request.POST, user=user)

    # ✅ Validate and save new password if valid
    # ✅ التحقق من صحة وحفظ كلمة مرور جديدة إذا كانت صالحة
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "success"})
    else:
        # ❌ Return errors if form is invalid
        # ❌ أخطاء الإرجاع إذا كان النموذج غير صالح
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


# 🌐 Friendship Request and Friends Management API
# 🌐 واجهة برمجية لإدارة طلبات الصداقة وإدارة الأصدقاء
@api_view(["POST"])
def send_friendship_request(request, pk):
    # 👤 Get the user to whom the friendship request is being sent
    # 👤 جلب المستخدم الذي يتم إرسال طلب الصداقة إليه
    user = User.objects.get(pk=pk)
    # For Test
    # print("How Is User Send Friend Ship Request", pk)
    # print("_______________________________________")

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    if not check1 or not check2:
        # ✉️ Create a new friendship request if it doesn't exist
        # ✉️ إنشاء طلب صداقة جديد إذا لم يكن موجودًا
        friendrequest = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )
        # For Test
        # print("Friend Ship Request If ", friendrequest)
        # print("_______________________________________")
        # Return = The Message Show In Frontend
        return JsonResponse({"message": "friendship request created"})
    else:
        # Return = The Message Show In Frontend
        return JsonResponse({"message": "request already sent"})


@api_view(["GET"])
def friends(request, pk):
    # 👥 Get the friends and requests for the specified user
    # 👥 جلب الأصدقاء والطلبات للمستخدم المحدد
    user = User.objects.get(pk=pk)
    # print("Friends User By Id 👉️", user)

    requests = []
    # print("Friends Requests By Id 👉️", requests)

    # 📝 Check if the current user is the requested user
    # 📝 التحقق مما إذا كان المستخدم الحالي هو نفس المستخدم المطلوب
    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.NOT_SENT
        )
        # print("requests Friends", requests)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

        # print("Friends Requests By Id 👉️", requests)

    # 👫 Retrieve all friends of the user
    # 👫 جلب جميع أصدقاء المستخدم
    friends = user.friends.all()
    # print("Friends Friends 👉️", friends)

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def my_friendship_suggestions(request):
    # 🤝 Suggest users the current user may know
    # 🤝 اقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)
    # print("🤝 Suggest users", serializer)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def handle_request(request, pk, status):
    # 🛠️ Handle and update the status of a friendship request
    # 🛠️ معالجة وتحديث حالة طلب الصداقة
    user = User.objects.get(pk=pk)
    # friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(
    #     created_by=user
    # )
    friendship_request = FriendshipRequest.objects.filter(
        created_for=request.user, created_by=user
    ).first()
    if not friendship_request:
        return JsonResponse(
            {"error": "Friendship request not found or already handled"}, status=404
        )
    # إذا كان يوجد طلب صداقة واحد فقط
    # friendship_request = friendship_requests.first()
    # استخدام first() بدلاً من get()

    if not friendship_request:
        return JsonResponse({"error": "Friendship request not found"}, status=404)

    friendship_request.status = status
    friendship_request.save()

    # 👥 Add each user to the other's friends list if accepted
    # 👥 إضافة كل مستخدم إلى قائمة أصدقاء الآخر إذا تم قبول الطلب
    user.friends.add(request.user)
    user.friends_count += 1
    user.save()

    request_user = request.user
    request_user.friends_count += 1
    request_user.save()

    # return JsonResponse({"message": "friendship request updated"})
    return JsonResponse({"message": f"Friendship request {status} successfully"})

```

### 🧑 Account Page [ urls.py ]

#### 🧑 App [ Account ] Page [ urls.py ] 📝

```python
urls.py
```

```python
# 📄 ملف [ messenger/messenger_django/account/urls.py ]

# 🌐 URL Configuration for User and Friend Management API
# 🌐 تكوين الروابط لواجهة برمجية لإدارة المستخدم والأصدقاء

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns = [
    # 👤 Retrieve current user's information استرجاع معلومات المستخدم الحالي
    path("me/", api.me, name="me"),
    # 📝 Signup for new users تسجيل مستخدمين جدد
    path("signup/", api.signup, name="signup"),
    # 🔑 Obtain JWT token for login الحصول على رمز JWT لتسجيل الدخول
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    # ♻️ Refresh JWT token تحديث رمز
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # ___________________________
    # ___________________________
    # ___________________________
    # Profile
    path("profile/<uuid:id>/", api.profile, name="profile"),
    # ✏️ Edit user profile تعديل ملف المستخدم
    path("editprofile/", api.editprofile, name="editprofile"),
    # 🔒 Change user password تغيير كلمة مرور المستخدم
    path("editpassword/", api.editpassword, name="editpassword"),
    # ___________________________
    # ___________________________
    # ___________________________
    # All Friends
    # 👫 Retrieve friends of a user  استرجاع أصدقاء المستخدم
    path("friends/<uuid:pk>/", api.friends, name="friends"),
    # 🤝 Retrieve suggested friends استرجاع الأصدقاء المقترحين
    path(
        "friends/suggested/",
        api.my_friendship_suggestions,
        name="my_friendship_suggestions",
    ),
    # ✉️ Send friendship request إرسال طلب صداقة
    path(
        "friends/<uuid:pk>/request/",
        api.send_friendship_request,
        name="send_friendship_request",
    ),
    # 🛠️ Handle friendship request (accept/reject) معالجة طلب الصداقة (قبول/رفض)
    path("friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"),
]
```

### ⚙️ Project Page [ urls.py ]

#### ⚙ Project Page [ urls.py ] 📝

```python
# 📄 ملف [ messenger/messenger_django/messenger_django/urls.py ]

# 🌐 Main URL Configuration for Django Project
# 🌐 تكوين الروابط الرئيسية لمشروع Django

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔗 Include URLs from the 'account' app for API endpoints
    # 🔗 تضمين روابط تطبيق 'account' للنقاط البرمجية
    path("api/", include("account.urls")),
    # 🔧 Admin panel for site management
    # 🔧 لوحة تحكم الإدارة لإدارة الموقع
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 🖼️ Serve media files during development
# 🖼️ عرض ملفات الوسائط أثناء التطوير

```

### 🧑 Create File Script

#### ⚙ Create Page [ generate_friend_suggestions.py ]

```python
scripts/generate_friend_suggestions.py
```

```python
# -*- coding: utf-8 -*-
# 🌐 تحديد نوع الترميز للملف كـ UTF-8 لدعم الأحرف غير اللاتينية.
# Set the file encoding to UTF-8 to support non-Latin characters.
# python scripts\generate_friend_suggestions.py

# 📚 استيراد مكتبة Django.
import django

# 📂 استيراد مكتبة os للتعامل مع نظام الملفات.
import os

# ⚙️ استيراد مكتبة sys للتعامل مع مسار Python والبيئة.
import sys

# ⏳ استيراد timedelta لحساب الفروقات الزمنية.
from datetime import timedelta

# 📊 استيراد Counter لحساب تكرار العناصر.
from collections import Counter

# 🕰️ استيراد timezone للتعامل مع التواريخ في Django.
from django.utils import timezone

# ➕ إضافة مسار المشروع الرئيسي إلى sys.path للتأكد من أن Python يمكنه العثور على الوحدات.
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

# ⚙️ إعداد متغير البيئة لاستخدام إعدادات Django.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messenger_django.settings")

# 🚀 تشغيل إعدادات Django.
django.setup()


# 👥 استيراد نموذج المستخدم من تطبيق account.
from account.models import User

# 🔍 الحصول على جميع المستخدمين في قاعدة البيانات.
users = User.objects.all()


# 🔄 حلقة تمر على كل مستخدم في القائمة.
for user in users:
    # 🧹 مسح قائمة "الأشخاص الذين قد تعرفهم" للمستخدم الحالي.
    # Clear the "people you may know" list for the current user.
    user.people_you_may_know.clear()

    # 🔁 حلقة تمر على كل صديق للمستخدم.
    for friend in user.friends.all():
        # 📝 طباعة رسالة توضح أن المستخدم صديق مع الشخص الحالي.
        print("User:", user, "Is Friend With 🧑 ", friend)
        print("________________________________________________________________")

        # 🔁 حلقة تمر على أصدقاء الصديق (أصدقاء أصدقائي).
        for friendsfriend in friend.friends.all():
            # 🔎 طباعة قائمة الأصدقاء المقترحين.
            # print("Checking Suggested Friend 👉️ ", friendsfriend)
            # print("________________________________________________________________")
            # طباعة جميع أصدقاء المستخدم.
            # print("All Friends user.friends.all() 👉️ ", user.friends.all())
            # print("________________________________________________________________")
            # تحقق من أن الصديق ليس المستخدم نفسه وليس ضمن أصدقائه الحاليين.
            # print("All friendsfriend != user 👉️ ", friendsfriend != user)
            # print("________________________________________________________________")
            if friendsfriend != user and friendsfriend not in user.friends.all():
                print(
                    "Adding friend suggestion for:",
                    user,
                    f"✔️  Suggested Friend:",
                    friendsfriend,
                )

                # إضافة الصديق المقترح إلى قائمة "الأشخاص الذين قد تعرفهم".
                user.people_you_may_know.add(friendsfriend)
                # print("Added to suggestions 👉️ ", friendsfriend)
                # print(
                #     "________________________________________________________________"
                # )

    # طباعة سطر فارغ للوضوح بين المستخدمين.
    # print("Updated suggestions for user:", user)
    # print("Suggestions:", user.people_you_may_know.all())
    # print("----------------------------------------------------")

print("Finished updating 'people you may know' for all users.")


"""
شرح الكود بشكل عام:
🔹 الوصف العام: الكود يمر على جميع المستخدمين في قاعدة البيانات، ثم يحلل أصدقاء كل مستخدم ويبحث عن أصدقاء أصدقائه لإضافتهم إلى قائمة "الأشخاص الذين قد تعرفهم"، بشرط ألا يكون هؤلاء الأصدقاء موجودين بالفعل في قائمة أصدقاء المستخدم أو أن يكونوا المستخدم نفسه.
"""

```

### 👤 Superuser

#### ⚙ Create Superuser

```cmd
python manage.py createsuperuser
```

```cmd
Email: learncodingeasy0100@gmail.com
Password: ******
Password (again): ******
Superuser created successfully.
```

### 🚀 Run Server

###### 🚀 Run Server

```cmd
python manage.py runserver
```

###### 👉️ Go To

---

```cmd
http://127.0.0.1:8000/
```

```cmd
http://127.0.0.1:8000/admin
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

## Vue

### 🖥️ Create Vue Project

###### 📁 Create Vue Project

```cmd
npm create vue@latest
```

###### 🚀 Choose Vite [ Project name & Select a framework] 🛠️

```cmd
√ Project name: ... messenger_vue
√ Add TypeScript? ... [No] / Yes
√ Add JSX Support? ... [No] / Yes
√ Add Vue Router for Single Page Application development? ... No / [Yes]
√ Add Pinia for state management? ... No / [Yes]
√ Add Vitest for Unit Testing? ... [No] / Yes
√ Add an End-to-End Testing Solution? » [No]
√ Add ESLint for code quality? ... No / [Yes]
√ Add Prettier for code formatting? ... No / [Yes]
√ Add Vue DevTools 7 extension for debugging? (experimental) ... [No] / Yes

Scaffolding project in E:\Projects\messenger\messenger_vue...

Done. Now run:
  cd messenger_vue
  npm install
  npm run format
  npm run build
  npm run dev
```

```cmd
cd messenger_vue
```

```cmd
npm install
```

```cmd
npm run format
```

```cmd
npm run build
```

```cmd
npm run dev
```

### 📚 Install Vue Libraries

###### 📚 Install Vue Libraries

- 1️⃣ Tailwind

```cmd
npm install -D tailwindcss postcss autoprefixer
```

```cmd
npx tailwindcss init -p
```

- 2️⃣ PrimeVue

```cmd
npm install primevue primeicons
```

```cmd
npm install @primevue/themes
```

```cmd
npm install quill
```

- 3️⃣ scss

```cmd
npm install -D sass@latest
```

- 4️⃣ Axios

```cmd
npm install axios
```

- 5️⃣ Font Awesome

```cmd
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons
```

- 6️⃣ Pwa

```cmd
npm install -D vite-plugin-pwa
```

- 7️⃣ Prism

```cmd
npm i prismjs
```

```cmd
npm i vue-prism-component
```

- 8️⃣ Swiper

```cmd
npm i swiper
```

- 9️⃣

```cmd

```
