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
