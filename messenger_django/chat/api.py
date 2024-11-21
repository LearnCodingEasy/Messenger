"""
هذا الكود يوضح كيفية إنشاء مجموعة من واجهات برمجة التطبيقات (APIs) للتعامل مع المحادثات والرسائل باستخدام Django REST Framework. إليك شرحًا تفصيليًا لكل دالة وما تقوم به:

1. دالة conversation_list
الهدف: عرض جميع المحادثات التي يشارك فيها المستخدم الحالي.
الخطوات:
تصفية المحادثات التي تحتوي على المستخدم الحالي باستخدام filter(users__in=list([request.user])).
تحويل البيانات باستخدام ConversationSerializer.
إرجاع البيانات بشكل JSON إلى العميل باستخدام JsonResponse.
2. دالة conversation_detail
الهدف: عرض تفاصيل محادثة معينة بناءً على معرف المحادثة (pk).
الخطوات:
جلب المحادثة باستخدام get(pk=pk) وتصفية المحادثات التي تحتوي على المستخدم الحالي.
تحويل بيانات المحادثة باستخدام ConversationDetailSerializer.
إرسال التفاصيل بشكل JSON إلى العميل.
3. دالة conversation_get_or_create
الهدف: جلب محادثة بين المستخدم الحالي ومستخدم آخر معين أو إنشاء محادثة جديدة إذا لم تكن موجودة.
الخطوات:
جلب المستخدم الآخر باستخدام User.objects.get(pk=user_pk).
تصفية المحادثات التي تضم كلا المستخدمين.
إذا كانت المحادثة موجودة، يتم استخدام أول محادثة موجودة. وإذا لم تكن موجودة، يتم إنشاء محادثة جديدة وإضافة المستخدمين إليها.
تحويل البيانات باستخدام ConversationDetailSerializer وإرسالها بشكل JSON.
4. دالة conversation_send_message
الهدف: إرسال رسالة داخل محادثة محددة.
الخطوات:
جلب المحادثة باستخدام get(pk=pk) والتأكد من أن المستخدم الحالي جزء من المحادثة.
تحديد المستخدم المستلم للرسالة.
إنشاء رسالة جديدة باستخدام ConversationMessage.objects.create.
تحويل الرسالة باستخدام ConversationMessageSerializer وإرجاعها بشكل JSON.
ملاحظات إضافية:
الديكور @api_view(["GET"]): يحدد أن الدالة هي API وتدعم طريقة GET (يمكن أيضًا أن تدعم POST أو غيرها).
JsonResponse: يستخدم لإرسال البيانات إلى العميل في شكل JSON.
معالجة الأخطاء: لم تتم معالجة حالات الخطأ مثل عدم العثور على مستخدم أو محادثة، ويفضل إضافة استثناءات للتحقق من الأخطاء مثل DoesNotExist.
تحسينات محتملة:
إضافة مصادقة (authentication_classes) وصلاحيات (permission_classes) لضمان أن المستخدمين مصرح لهم بالوصول إلى هذه الدوال.
التعامل مع حالات الخطأ باستخدام try-except لإرجاع استجابات مناسبة مثل Http404 أو استجابة خطأ مخصصة.
هذا الكود يوفر بنية مرنة وسهلة للتعامل مع المحادثات والرسائل في تطبيقات الدردشة باستخدام Django REST Framework.

"""

from django.http import JsonResponse

# 📝 لتحديد أن هذه الدالة هي API view
# 🔐 لتحديد الكلاسات المسؤولة عن المصادقة
# 🔑 لتحديد الكلاسات المسؤولة عن الصلاحيات
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# 👤 استيراد نموذج المستخدم من التطبيق
from account.models import User

# 💬 استيراد النماذج الخاصة بالمحادثات والرسائل
from .models import (
    Conversation,
    ConversationMessage,
)

# 🧩 تعريف السيريالايزر للمحادثات
# 🔍 سيريالايزر لعرض تفاصيل المحادثة
# 📝 سيريالايزر لعرض تفاصيل الرسائل
from .serializers import (
    ConversationSerializer,
    ConversationDetailSerializer,
    ConversationMessageSerializer,
)


# 🚀 هذا الديكور يتم تطبيقه لتحديد أن هذه دالة GET API
# 📋 دالة لعرض جميع المحادثات الخاصة بالمستخدم
@api_view(["GET"])
def conversation_list(request):
    # 🧐 تصفية المحادثات التي تضم المستخدم الحالي
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    # 🧩 تحويل البيانات إلى الشكل المناسب
    serializer = ConversationSerializer(conversations, many=True)

    # 📡 إرسال البيانات إلى العميل في شكل JSON
    return JsonResponse(serializer.data, safe=False)


# 🚀 دالة لعرض تفاصيل محادثة معينة
# 🔑 تحديد المحادثة باستخدام الـ pk
@api_view(["GET"])
def conversation_detail(request, pk):
    # 🕵️‍♂️ جلب المحادثة باستخدام الـ pk
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(
        pk=pk
    )
    # 🔍 تحويل بيانات المحادثة إلى الشكل المناسب
    serializer = ConversationDetailSerializer(conversation)

    # 📡 إرسال التفاصيل إلى العميل
    return JsonResponse(serializer.data, safe=False)


# 🚀 دالة للحصول على محادثة أو إنشائها إذا لم تكن موجودة
# 👤 المستخدم المستهدف الذي سنتحقق من وجود محادثة معه
@api_view(["GET"])
def conversation_get_or_create(request, user_pk):
    # 🔍 جلب المستخدم المستهدف باستخدام الـ pk
    user = User.objects.get(pk=user_pk)

    # 🧐 تصفية المحادثات التي تضم المستخدمين
    conversations = Conversation.objects.filter(users__in=list([request.user])).filter(
        users__in=list([user])
    )

    # ✅ إذا كانت المحادثة موجودة
    if conversations.exists():
        # 🔄 أخذ أول محادثة موجودة
        conversation = conversations.first()
    # 🚫 إذا لم تكن المحادثة موجودة
    else:
        # 🛠 إنشاء محادثة جديدة
        conversation = Conversation.objects.create()
        # 👥 إضافة المستخدمين إلى المحادثة
        conversation.users.add(user, request.user)
        # 💾 حفظ المحادثة الجديدة
        conversation.save()

    # 🧩 تحويل البيانات إلى الشكل المناسب
    serializer = ConversationDetailSerializer(conversation)

    # 📡 إرسال البيانات إلى العميل
    return JsonResponse(serializer.data, safe=False)


# 🚀 دالة لإرسال رسالة داخل المحادثة
# 💬 إرسال رسالة إلى المحادثة المحددة
@api_view(["POST"])
def conversation_send_message(request, pk):
    # 🕵️‍♂️ جلب المحادثة باستخدام الـ pk
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(
        pk=pk
    )

    # 👥 التحقق من جميع المستخدمين في المحادثة
    for user in conversation.users.all():
        # ❌ استبعاد المستخدم الحالي
        if user != request.user:
            # 📤 تحديد المستلم
            sent_to = user

    conversation_message = ConversationMessage.objects.create(
        # ✉️ إنشاء الرسالة
        conversation=conversation,
        # 📝 جلب نص الرسالة من البيانات المدخلة
        body=request.data.get("body"),
        # 🖊️ تحديد من أنشأ الرسالة
        created_by=request.user,
        # 📬 تحديد من أُرسلت إليه الرسالة
        sent_to=sent_to,
    )

    # 🧩 تحويل البيانات إلى الشكل المناسب
    serializer = ConversationMessageSerializer(conversation_message)

    # 📡 إرسال الرسالة إلى العميل
    return JsonResponse(serializer.data, safe=False)
