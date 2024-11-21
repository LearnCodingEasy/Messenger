"""
هذا الكود يوضح كيفية إعداد مسارات الـ URLs لتطبيق محادثات في Django باستخدام دالة path. إليك شرحًا تفصيليًا للرمز:

1. استيراد path
يتم استيراد دالة path من django.urls لإنشاء مسارات الـ URLs الخاصة بالتطبيق.
2. استيراد وحدة api
يتم استيراد وحدة api من نفس التطبيق الذي يحتوي على الدوال (واجهات برمجة التطبيقات) التي تم تعريفها سابقًا مثل conversation_list و conversation_detail.
3. قائمة urlpatterns
قائمة تحتوي على جميع المسارات المتاحة التي يقدمها التطبيق.
تفاصيل كل مسار:
عرض قائمة المحادثات

المسار: "" (المسار الرئيسي للتطبيق).
الدالة المستدعاة: api.conversation_list.
الاسم: conversation_list لتسهيل الرجوع إلى هذا المسار في أماكن أخرى من التطبيق.
عرض تفاصيل المحادثة

المسار: "<uuid:pk>/"، حيث يتم تمرير الـ UUID الخاص بالمحادثة كجزء من الـ URL.
الدالة المستدعاة: api.conversation_detail.
الاسم: conversation_detail.
إرسال رسالة جديدة في المحادثة

المسار: "<uuid:pk>/send/".
الدالة المستدعاة: api.conversation_send_message.
الاسم: conversation_send_message.
الحصول على محادثة مع مستخدم أو إنشاؤها

المسار: "<uuid:user_pk>/get-or-create/".
الدالة المستدعاة: api.conversation_get_or_create.
الاسم: conversation_get_or_create.
ملاحظات إضافية:
يتم استخدام الـ UUID في المسارات لتحديد المحادثات والمستخدمين بشكل فريد.
هذه المسارات تستخدم دوال API التي تم تعريفها مسبقًا وتعيد استجابات JSON.
تحسينات محتملة:
يمكن إضافة مصادقة وصلاحيات عند استدعاء هذه الدوال لضمان أمان التطبيق.
يمكن إضافة استثناءات مخصصة للتعامل مع الأخطاء مثل Http404.
هذا الكود يُعتبر جزءًا أساسيًا من أي تطبيق يعتمد على نظام المحادثات، حيث يوفر واجهات واضحة للوصول إلى المحادثات، عرض التفاصيل، وإرسال الرسائل.

"""

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
