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
        fields = ("id", "created_by", "status")
