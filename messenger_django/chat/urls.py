# 🛤️ استيراد دالة `path` لإنشاء مسارات URL
from django.urls import path

# 📦 استيراد وحدة `api` من نفس التطبيق
from . import api

# 🗺️ قائمة `urlpatterns` لتحديد جميع مسارات الـ URL التي يقدمها التطبيق
urlpatterns = [
    # 📋 عرض قائمة المحادثات (المسار الرئيسي)
    path("", api.conversation_list, name="conversation_list"),
    # 🔍 عرض تفاصيل المحادثة بناءً على الـ UUID الخاص بها
    path("<uuid:pk>/", api.conversation_detail, name="conversation_detail"),
    # ✉️ إرسال رسالة جديدة في المحادثة المحددة
    # 📝 استدعاء دالة `conversation_send_message` من وحدة `api`
    # 🏷️ اسم المسار لتحديده في أماكن أخرى
    path(
        "<uuid:pk>/send/",
        api.conversation_send_message,
        name="conversation_send_message",
    ),
    # 🛠️ الحصول على محادثة مع مستخدم أو إنشاؤها إذا لم تكن موجودة
    # 🔄 استدعاء دالة `conversation_get_or_create` من وحدة `api`
    # 🏷️ اسم المسار لاستخدامه في أماكن أخرى من التطبيق
    path(
        "<uuid:user_pk>/get-or-create/",
        api.conversation_get_or_create,
        name="conversation_get_or_create",
    ),
]
