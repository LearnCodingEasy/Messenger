"""
هذا الكود يحتوي على serializers من مكتبة Django REST Framework، وهو يستخدم لتحويل البيانات بين نماذج Django وواجهة برمجة التطبيقات (JSON). يتم استخدام هذه المحولات لتهيئة البيانات التي تُعرض للمستخدمين أو تُستقبل منهم بشكل منظم.

شرح كل جزء من الكود:
1. استيراد المكتبات والموارد:
serializers من rest_framework: تُستخدم لإنشاء محولات البيانات.
UserSerializer من account.serializers: محول بيانات خاص بنموذج المستخدم.
نماذج Conversation وConversationMessage من .models: هي النماذج التي نريد تحويلها.
2. ConversationSerializer
الهدف: لتحويل نموذج المحادثة (Conversation) إلى JSON.
الحقل users:
يستخدم UserSerializer لعرض تفاصيل المستخدمين المرتبطين بالمحادثة.
الخاصية read_only=True تعني أن البيانات لا يمكن تعديلها من خلال هذا المحول.
many=True تعني أن الحقل يحتوي على قائمة من المستخدمين.
الفئة Meta:
تحدد النموذج المستخدم (Conversation).
تحدد الحقول التي سيتم تضمينها عند تحويل البيانات:
id: معرف المحادثة.
users: المستخدمون المشاركون.
modified_at_formatted: الوقت المنقضي منذ تعديل المحادثة.
3. ConversationMessageSerializer
الهدف: لتحويل نموذج الرسالة (ConversationMessage) إلى JSON.
الحقل sent_to و created_by**:
يستخدمان UserSerializer لعرض تفاصيل المستخدم الذي أُرسلت له الرسالة والمستخدم الذي أنشأ الرسالة.
read_only=True لأن هذه الحقول تُعرض فقط ولا يمكن تعديلها.
الفئة Meta:
تحدد النموذج المستخدم (ConversationMessage).
تحدد الحقول التي سيتم تضمينها عند تحويل البيانات:
id: معرف الرسالة.
sent_to: المستخدم المرسل إليه.
created_by: المستخدم الذي أرسل الرسالة.
created_at_formatted: الوقت المنقضي منذ إرسال الرسالة.
body: محتوى الرسالة.
4. ConversationDetailSerializer
الهدف: لعرض تفاصيل المحادثة مع الرسائل المرتبطة بها.
الحقل messages:
يستخدم ConversationMessageSerializer لتحويل الرسائل المرتبطة بالمحادثة.
read_only=True و many=True، مما يعني أنه يعرض قائمة من الرسائل ولا يمكن تعديلها.
الفئة Meta:
تحدد النموذج المستخدم (Conversation).
تحدد الحقول التي سيتم تضمينها عند تحويل البيانات:
id: معرف المحادثة.
users: المستخدمون المشاركون.
modified_at_formatted: الوقت المنقضي منذ تعديل المحادثة.
messages: الرسائل المرتبطة بالمحادثة.
ملخص:
هذه المحولات تساعد في تسهيل التعامل مع بيانات المحادثات والرسائل في واجهة برمجة التطبيقات، حيث تعرض البيانات بطريقة منسقة ومفصلة للمستخدمين.
read_only=True يضمن أن البيانات تُعرض فقط ولا يمكن تعديلها عبر واجهة برمجة التطبيقات.

"""

# 📝 Page [ messenger/messenger_django/chat/serializers.py ]

from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Conversation, ConversationMessage


class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = (
            "id",
            "users",
            "modified_at_formatted",
        )


class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = (
            "id",
            "sent_to",
            "created_by",
            "created_at_formatted",
            "body",
        )


class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = (
            "id",
            "users",
            "modified_at_formatted",
            "messages",
        )
