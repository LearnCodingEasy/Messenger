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
