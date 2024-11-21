# استيراد uuid لإنشاء معرّفات فريدة
# Import uuid to generate unique identifiers
import uuid

# استيراد النماذج من Django
# Import models from Django
from django.db import models

# استيراد الدالة timesince لتنسيق الوقت
# Import the timesince function to format time
from django.utils.timesince import timesince

# استيراد نموذج المستخدم
# Import the User model
from account.models import User


# نموذج المحادثة
# Conversation model
class Conversation(models.Model):
    # معرف فريد للمحادثة
    # Unique identifier for the conversation
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # علاقة ManyToMany مع المستخدمين
    # Many-to-many relationship with users
    # هذه العلاقة تسمح بوجود العديد من المستخدمين في نفس المحادثة
    # This relationship allows multiple users to be part of the same conversation
    users = models.ManyToManyField(User, related_name="conversations")

    # تاريخ ووقت إنشاء المحادثة
    # Date and time when the conversation was created
    # يتم تحديد تاريخ ووقت الإنشاء تلقائيًا عند إضافة المحادثة
    # The created_at field is set automatically when the conversation is created
    created_at = models.DateTimeField(auto_now_add=True)

    # تاريخ ووقت آخر تعديل للمحادثة
    # Date and time of the last modification of the conversation
    # يتم تحديث هذا الحقل تلقائيًا عند أي تعديل على المحادثة
    # This field gets updated automatically on any modification of the conversation
    modified_at = models.DateTimeField(auto_now=True)

    # دالة لإرجاع الوقت المنقضي منذ إنشاء المحادثة بتنسيق قابل للقراءة البشرية
    # Method to return the time elapsed since the conversation was created in a human-readable format
    # تستخدم هذه الدالة دالة timesince لعرض الفرق بين تاريخ الإنشاء والوقت الحالي
    # This method uses the timesince function to display the difference between creation time and current time
    def modified_at_formatted(self):
        return timesince(self.created_at)


# نموذج الرسالة في المحادثة
# Conversation message model
class ConversationMessage(models.Model):
    # معرف فريد للرسالة
    # Unique identifier for the message
    # يتم تعيين معرف فريد لكل رسالة باستخدام UUID
    # Each message is assigned a unique identifier using UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # علاقة ForeignKey مع المحادثة التي تنتمي إليها الرسالة
    # ForeignKey relationship to the conversation that the message belongs to
    # هذه العلاقة تشير إلى المحادثة التي تنتمي إليها الرسالة
    # This relationship points to the conversation that the message belongs to
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )

    # نص الرسالة
    # The actual text content of the message
    # يتم تخزين النص الكامل للرسالة في هذا الحقل
    # The full text of the message is stored in this field
    body = models.TextField()

    # علاقة ForeignKey مع المستخدم الذي استلم الرسالة
    # ForeignKey relationship to the user who received the message
    # هذا الحقل يشير إلى المستخدم الذي تلقى الرسالة
    # This field points to the user who received the message
    sent_to = models.ForeignKey(
        User, related_name="received_messages", on_delete=models.CASCADE
    )

    # تاريخ ووقت إرسال الرسالة
    # Date and time when the message was sent
    # يتم تعيين تاريخ ووقت الإرسال تلقائيًا عند إرسال الرسالة
    # The created_at field is set automatically when the message is sent
    created_at = models.DateTimeField(auto_now_add=True)

    # علاقة ForeignKey مع المستخدم الذي أرسل الرسالة
    # ForeignKey relationship to the user who sent the message
    # هذا الحقل يشير إلى المستخدم الذي أرسل الرسالة
    # This field points to the user who sent the message
    created_by = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.CASCADE
    )

    # دالة لإرجاع الوقت المنقضي منذ إرسال الرسالة بتنسيق قابل للقراءة البشرية
    # Method to return the time elapsed since the message was sent in a human-readable format
    # تستخدم هذه الدالة دالة timesince لعرض الفرق بين تاريخ الإرسال والوقت الحالي
    # This method uses the timesince function to display the difference between sent time and current time
    def created_at_formatted(self):
        return timesince(self.created_at)


"""
هذا الكود عبارة عن نماذج (models) مخصصة لنظام دردشة في مشروع Django، حيث يحتوي على نموذجين رئيسيين: Conversation و ConversationMessage. إليك شرحًا تفصيليًا:

1. استيراد المكتبات والموارد:
uuid: لإنشاء معرفات فريدة (UUID) تُستخدم لتعريف المحادثات والرسائل بشكل فريد.
models من django.db: لإنشاء نماذج قاعدة البيانات.
timesince من django.utils.timesince: دالة لعرض الفرق الزمني بصيغة قابلة للقراءة البشرية.
نموذج User من account.models: يشير إلى مستخدم في النظام.
2. نموذج المحادثة (Conversation):
الحقل id:
نوع الحقل: UUIDField.
يستخدم لتعيين معرف فريد لكل محادثة.
يحدد تلقائيًا باستخدام uuid4.
الحقل users:
نوع العلاقة: ManyToManyField.
يشير إلى علاقة بين المحادثة والعديد من المستخدمين، مما يسمح بوجود عدة مستخدمين في نفس المحادثة.
الحقل created_at:
نوع الحقل: DateTimeField.
يتم تحديد تاريخ ووقت إنشاء المحادثة تلقائيًا عند حفظها لأول مرة.
الحقل modified_at:
نوع الحقل: DateTimeField.
يتم تحديث هذا الحقل تلقائيًا عند أي تعديل في المحادثة.
الدالة modified_at_formatted:
تعرض الوقت المنقضي منذ إنشاء المحادثة باستخدام دالة timesince.
3. نموذج الرسالة (ConversationMessage):
الحقل id:
نوع الحقل: UUIDField.
معرف فريد لكل رسالة.
الحقل conversation:
نوع العلاقة: ForeignKey.
يشير إلى المحادثة التي تنتمي إليها الرسالة.
يتم حذف الرسالة إذا تم حذف المحادثة المرتبطة بها (on_delete=models.CASCADE).
الحقل body:
نوع الحقل: TextField.
يحتوي على النص الكامل للرسالة.
الحقل sent_to:
نوع العلاقة: ForeignKey.
يشير إلى المستخدم الذي تلقى الرسالة.
الحقل created_at:
نوع الحقل: DateTimeField.
يتم تعيين وقت وتاريخ الإرسال تلقائيًا عند إنشاء الرسالة.
الحقل created_by:
نوع العلاقة: ForeignKey.
يشير إلى المستخدم الذي أرسل الرسالة.
الدالة created_at_formatted:
تعرض الوقت المنقضي منذ إرسال الرسالة باستخدام timesince.
ملخص:
الكود يُعرّف نموذجًا للمحادثات يتيح للمستخدمين المشاركة في محادثات جماعية.
كل رسالة في المحادثة ترتبط بمستخدمين (المرسل والمتلقي) وتشير إلى المحادثة الأم.
الحقول الزمنية تسجل وقت الإنشاء والتعديل، ويتم عرض الفارق الزمني بطريقة مفهومة للبشر عبر دوال تنسيق الوقت.

"""
