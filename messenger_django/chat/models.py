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
