# 📄 صفحة [trello/trello_django/account/models.py]
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
    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    # 📅 Join Date & Last Login تاريخ الانضمام وآخر تسجيل دخول و حالة الاتصال
    # Automatic
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)

    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
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
    # مهارات
    skills = models.JSONField(default=list, blank=True, null=True)
    # 📋 Tasks and Their Number المهام وعددها
    task_count = models.IntegerField(default=0)
    # 📅 User Is Online  حالة الاتصال
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

    def last_login_formatted(self):
        return timesince(self.last_login)


# 📬 Friend Request Form نموذج طلب الصداقة
class FriendshipRequest(models.Model):
    # 📝 Friend request cases  حالات طلب الصداقة
    NOTSEND = "notsend"  # 🚫 لم يتم الإرسال
    SEND = "send"  # ✉️ تم الإرسال
    WAITING = "waiting"  # ⏳ في انتظار الرد
    ACCEPTED = "accepted"  # ✅ تم القبول
    REJECTED = "rejected"  # ❌ تم الرفض
    CANCEL = "cancel"  # 🔄 تم الإلغاء
    BLOCKED = "blocked"  # 🚫 الحظر
    MUTED = "muted"  # 🔕 الكتم
    FROZEN = "frozen"  # 🧊 تجميد
    ARCHIVED = "archived"  # 📦 مؤرشف
    FOLLOWING = "following"  # 👥 متابعة
    UNFOLLOWED = "unfollowed"  # 🚫 إلغاء المتابعة
    REPORTED = "reported"  # 🚨 تم الإبلاغ عنه
    SPAM = "spam"  # 🗑️ بريد مزعج
    DELETED = "deleted"  # 🗑️ محذوف
    FAVORITE = "favorite"  # 🌟 مفضل
    TEMPORARILY_BLOCKED = "temporarily_blocked"  # ⏳ حظر مؤقت
    VERIFIED = "verified"  # ✔️ تم التحقق
    REQUEST_RESENT = "request_resent"  # 🔄 تم إعادة الإرسال
    SUGGESTED = "suggested"  # 💡 مقترح
    IGNORED = "ignored"  # 🛑 تم التجاهل
    INACTIVE = "inactive"  # ⚠️ غير نشط
    LIMITED = "limited"  # 🚫 محدود

    # 📜 قائمة الحالات الممكنة مع النصوص المقابلة
    STATUS_CHOICES = (
        (NOTSEND, "NotSent"),  # 🚫 لم يتم الإرسال
        (SEND, "Send"),  # ✉️ تم الإرسال
        (WAITING, "Waiting"),  # ⏳ في انتظار الرد
        (ACCEPTED, "Accepted"),  # ✅ تم القبول
        (REJECTED, "Rejected"),  # ❌ تم الرفض
        (CANCEL, "Cancel"),  # 🔄 تم الإلغاء
        (BLOCKED, "Blocked"),  # 🚫 الحظر
        (MUTED, "Muted"),  # 🔕 الكتم
        (FROZEN, "Frozen"),  # 🧊 تجميد
        (ARCHIVED, "Archived"),  # 📦 مؤرشف
        (FOLLOWING, "Following"),  # 👥 متابعة
        (UNFOLLOWED, "Unfollowed"),  # 🚫 إلغاء المتابعة
        (REPORTED, "Reported"),  # 🚨 تم الإبلاغ عنه
        (SPAM, "Spam"),  # 🗑️ بريد مزعج
        (DELETED, "Deleted"),  # 🗑️ محذوف
        (FAVORITE, "Favorite"),  # 🌟 مفضل
        (TEMPORARILY_BLOCKED, "TemporarilyBlocked"),  # ⏳ حظر مؤقت
        (VERIFIED, "Verified"),  # ✔️ تم التحقق
        (REQUEST_RESENT, "RequestResent"),  # 🔄 تم إعادة الإرسال
        (SUGGESTED, "Suggested"),  # 💡 مقترح
        (IGNORED, "Ignored"),  # 🛑 تم التجاهل
        (INACTIVE, "Inactive"),  # ⚠️ غير نشط
        (LIMITED, "Limited"),  # 🚫 محدود
    )

    # 🔑 Friend Request UUID Essential Field حقل أساسي UUID لطلب الصداقة
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 🧑 User receiving the request  المستخدم المستلم للطلب
    created_for = models.ForeignKey(
        User, related_name="received_friendshiprequests", on_delete=models.CASCADE
    )
    # 🧑 The user who sent the request  المستخدم المرسل للطلب
    created_by = models.ForeignKey(
        User, related_name="created_friendshiprequests", on_delete=models.CASCADE
    )
    # 📅 Creation date تاريخ الإنشاء
    created_at = models.DateTimeField(auto_now_add=True)
    # 📝 Order Status  حالة الطلب
    # 🚫 الحالة الافتراضية: "لم يتم الإرسال"
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOTSEND)

    # - 🔄 يتم استخدام عبارة "ترتيب حسب" لتحديد ترتيب البيانات المُسترجعة
    # - 📊 يمكن تحديد ترتيب البيانات بناءً على أحد الحقول في الجدول
    # - 🎚️ يتيح ذلك تنظيم البيانات بطريقة محددة، مثل الترتيب تصاعديًا أو تنازليًا
    class Meta:
        ordering = ("-created_at",)

    # - 🔍 اسم الاوبجكت اللى يظهر فى صفحة الادمان
    def __str__(self):
        return "%s" % self.status

    # 🔍 Retrieve All Friend Requests by User and Status 🔍
    # 🧑‍🤝‍🧑 جلب جميع طلبات الصداقة بناءً على المستخدم والحالة
    @staticmethod
    def get_friends_by_status(user, status):
        """جلب الأصدقاء بناءً على حالة محددة"""
        if status == FriendshipRequest.ACCEPTED:
            return User.objects.filter(
                received_friendshiprequests__created_by=user,
                received_friendshiprequests__status=status,
            ) | User.objects.filter(
                created_friendshiprequests__created_for=user,
                created_friendshiprequests__status=status,
            )
        return User.objects.filter(
            received_friendshiprequests__created_by=user,
            received_friendshiprequests__status=status,
        )
