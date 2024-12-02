# 📄 ملف [ messenger/messenger_django/account/api.py ]

# 🌐 API for User Signup and Profile Info Retrieval
# 🌐 API لتسجيل المستخدم واسترجاع معلومات الحساب

# Django إستيراد إعدادات المشروع في
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm, ProfileForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User, FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer, FriendshipRequestSerializer


import logging
from django.core.exceptions import PermissionDenied

# 🌐 إعداد مكتبة التسجيل
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from rest_framework.parsers import JSONParser


# 📝 Signup API Endpoint
# 📝 واجهة برمجية للتسجيل
@api_view(["POST"])  # 📬 السماح فقط بالطلبات من نوع POST.
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def signup(request):
    """
    وظيفة للتعامل مع تسجيل المستخدم.
    """
    # 🗃️ البيانات المُرسلة مع الطلب.
    data = request.data
    message = "success"

    # 🧾 Initialize signup form with request data
    # 🧾 تهيئة نموذج التسجيل باستخدام بيانات الطلب
    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    # ✅ Check if form is valid ✅ التحقق من صحة النموذج
    if form.is_valid():
        # 🛠️ Save the new user 🛠️ حفظ المستخدم الجديد
        user = form.save()
        # 🔓 Activate the account 🔓 تنشيط الحساب مباشرة
        user.is_active = True
        user.save()

        # 📤 إرجاع رسالة نجاح.
        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # ❌ If errors exist, return them ❌ إذا كان هناك أخطاء
        message = form.errors.as_json()
    # 🔍 Print errors for debugging 🔍 طباعة الأخطاء لأغراض التصحيح
    print(message)
    return JsonResponse({"message": message}, safe=False)


# 👤 User Info API Endpoint 👤 واجهة برمجية لاسترجاع معلومات المستخدم
@api_view(["GET", "POST"])
def me(request):
    """
    وظيفة لاسترجاع بيانات المستخدم الحالي.
    """
    # ✅ إذا كان المستخدم مصادقًا.
    if request.user.is_authenticated:
        # 📜 تحويل بيانات المستخدم إلى JSON.
        user_serializer = UserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)
    # ❌ إرجاع رسالة خطأ إذا كان المستخدم غير مصادق.
    return JsonResponse({"error": "User not authenticated"}, status=401)


# 📝 Profile API Endpoint
# 📝 واجهة برمجية لاسترجاع بيانات المستخدم
@api_view(["GET"])  # 🌐 السماح فقط بطلبات GET.
def profile(request, id):
    """
    وظيفة لاسترجاع بيانات ملف المستخدم بناءً على معرفه الفريد (ID).
    """
    user = User.objects.get(pk=id)
    print("Profile User By Id 👉️", user)

    # 📜 تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص.
    user_serializer = UserSerializer(user)
    # 🟢 افتراض أن المستخدم يمكنه إرسال طلب صداقة.
    can_send_friendship_request = True
    # 🔒 التحقق مما إذا كان المستخدم بالفعل صديقًا.
    if request.user in user.friends.all():
        can_send_friendship_request = False  # 🛑 لا يمكن إرسال طلب صداقة.

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # 🔴 إذا كان هناك طلب صداقة موجود، لا يمكن إرسال طلب جديد.
    if check1 or check2:
        can_send_friendship_request = False

    # 📤 إرجاع بيانات المستخدم وصلاحية إرسال طلب الصداقة كاستجابة JSON.
    return JsonResponse(
        {
            "user": user_serializer.data,  # بيانات المستخدم المسلسلة.
            "can_send_friendship_request": can_send_friendship_request,  # صلاحية إرسال طلب الصداقة.
        },
        safe=False,  # ⚠️ يتيح إرجاع البيانات غير المهيكلة كـ JSON.
    )


# 📝 واجهة برمجية لتعديل الملف الشخصي
@api_view(["POST"])  # 🌐 هذه الدالة تستجيب فقط لطلبات POST
def editprofile(request):
    # 👤 استرجاع بيانات المستخدم الحالي من الطلب
    # 👤 `request.user` تمثل المستخدم الذي أرسل الطلب
    user = request.user

    # 📧 الحصول على البريد الإلكتروني الجديد المرسل مع الطلب
    # 📧 يتم استخدام `request.data.get` للحصول على قيمة الحقل "email"
    email = request.data.get("email")

    # 📧 التحقق إذا كان البريد الإلكتروني مستخدمًا بالفعل من قبل مستخدم آخر
    # 📧 يتم استبعاد المستخدم الحالي من البحث باستخدام `exclude(id=user.id)`
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        # 🔴 إذا تم العثور على البريد الإلكتروني بالفعل، يتم إرجاع رسالة خطأ
        return JsonResponse({"message": "email already exists"})
    else:
        # 📝 تهيئة نموذج تعديل الملف الشخصي
        # 📝 يتم تمرير البيانات من الطلب (`request.POST`) وأي ملفات (`request.FILES`)
        # 📝 `instance=user` يربط النموذج بالمستخدم الحالي لتعديل بياناته
        form = ProfileForm(request.POST, request.FILES, instance=user)

        # ✅ Validate and save profile if valid
        # ✅ التحقق من صحة النموذج
        # ✅ إذا كانت البيانات صالحة، يتم حفظ التعديلات في قاعدة البيانات
        if form.is_valid():
            form.save()

        # 🔄 تسلسل بيانات المستخدم المحدثة
        # 🔄 يتم استخدام `UserSerializer` لتحويل بيانات المستخدم إلى صيغة JSON
        serializer = UserSerializer(user)

        # 🔄 إرجاع رسالة نجاح تحتوي على بيانات المستخدم المحدثة
        return JsonResponse({"message": "information updated", "user": serializer.data})


# 🛠️ واجهة برمجية لتغيير كلمة المرور
@api_view(["POST"])  # 🌐 الدالة تقبل فقط طلبات POST
def editpassword(request):
    # 🔒 تهيئة نموذج تغيير كلمة المرور
    # 🔒 `PasswordChangeForm` هو نموذج افتراضي من Django لتغيير كلمة المرور
    # 🔒 يتم تمرير بيانات الطلب (`request.POST`) والمستخدم الحالي (`user`)
    user = request.user
    form = PasswordChangeForm(data=request.POST, user=user)

    # ✅ Validate and save new password if valid
    # ✅ التحقق من صحة البيانات في النموذج
    if form.is_valid():
        # 🛠️ إذا كانت البيانات صالحة، يتم حفظ كلمة المرور الجديدة
        form.save()
        # 🟢 إرجاع استجابة نجاح للعميل
        return JsonResponse({"message": "success"})
    else:
        # ❌ Return errors if form is invalid
        # ❌ إذا كانت البيانات غير صالحة، يتم إرجاع الأخطاء
        # 🔍 يتم استخدام `form.errors.as_json()` لتحويل الأخطاء إلى صيغة JSON
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


# ___________________________
# ___________________________
# ___________________________


# 🌐 واجهة برمجية لجلب الأصدقاء وطلبات الصداقة لمستخدم معين
@api_view(["GET"])  # 🌐 الدالة تقبل فقط طلبات GET
def friends(request, pk):

    # 👤🎯 pk المستخدم اللى فاتح صفحة البروافيل عن طريق
    # User Pk [Id 🔑 ] الايدى الخاص بى المستخدام اللى انا بجيب الاصدقاء الخاصين بية
    user = User.objects.get(pk=pk)
    # print(f"user 🔋 {user}")
    # print("_________________________________✅_______________________________")

    # ✅ التحقق مما إذا كان المستخدم الحالي هو نفسه المستخدم الهدف
    is_current_user = user == request.user
    # print(f"request.user {request.user}")
    # print("_________________________________✅_______________________________")
    # print(f"is_current_user {is_current_user}")
    # print("_________________________________✅_______________________________")
    # 🟢 افتراض أن المستخدم يمكنه إرسال طلب صداقة.
    can_send_friendship_request = True
    # 🔒 التحقق مما إذا كان المستخدم بالفعل صديقًا.
    if request.user in user.friends.all():
        can_send_friendship_request = False  # 🛑 لا يمكن إرسال طلب صداقة.

    # 📝 جلب طلبات الصداقة إذا كان المستخدم الحالي هو نفسه الهدف
    requests = []
    if is_current_user:
        requests = FriendshipRequest.objects.filter(
            # target=request.user, status="notsend"
            created_for=request.user,
            status=FriendshipRequest.WAITING,
        )
        # 🔄 تحويل الطلبات إلى JSON باستخدام Serializer 🔄 تحويل الطلبات إلى بيانات JSON باستخدام السيريالايزر
        requests = FriendshipRequestSerializer(requests, many=True).data
        # print(f"Requests Friends  {requests}")
        # print("_________________________________✅_______________________________")

    # 👫 Retrieve all friends of the user 👫 جلب جميع أصدقاء المستخدم
    friendsAll = user.friends.all()
    # print(f"friendsAll {friendsAll}")
    # print("_________________________________✅_______________________________")
    # print("Friends Friends 👉️", friends)
    accepted_friends = FriendshipRequest.get_friends_by_status(
        user, FriendshipRequest.ACCEPTED
    )
    waiting_friends = FriendshipRequest.get_friends_by_status(
        user, FriendshipRequest.WAITING
    )
    rejected_friends = FriendshipRequest.get_friends_by_status(
        user, FriendshipRequest.REJECTED
    )
    cancelled_requests = FriendshipRequest.get_friends_by_status(
        user, FriendshipRequest.CANCEL
    )
    send = FriendshipRequest.get_friends_by_status(user, FriendshipRequest.SEND)
    # إضافة الأشخاص الذين لا يوجد بينهم طلب صداقة
    # اضافة جميع المستخدمين اللى سجلو الدخول فى الموقع
    notsend = FriendshipRequest.get_friends_by_status(user, FriendshipRequest.NOTSEND)
    notsend_users = User.objects.exclude(id__in=[friend.id for friend in friendsAll])

    # 📤 إرجاع البيانات كاستجابة JSON تحتوي على بيانات المستخدم، الأصدقاء، والطلبات
    return JsonResponse(
        {
            "user": UserSerializer(user).data,  # بيانات المستخدم
            # "friends": UserSerializer(friends, many=True).data,  # بيانات الأصدقاء
            "friends": {
                "accepted": UserSerializer(accepted_friends, many=True).data,
                "all": UserSerializer(friendsAll, many=True).data,
                "cancel": UserSerializer(cancelled_requests, many=True).data,
                "notsend": UserSerializer(notsend_users, many=True).data,
                "rejected": UserSerializer(rejected_friends, many=True).data,
                "send": UserSerializer(send, many=True).data,
                "waiting": UserSerializer(waiting_friends, many=True).data,
            },
            "requests": requests,  # طلبات الصداقة (إذا كانت موجودة)
            "can_send_friendship_request": can_send_friendship_request,  # صلاحية إرسال طلب الصداقة.
        },
        safe=False,  # السماح بتمرير كائنات ليست من نوع القاموس
    )


@api_view(["POST"])  # 🌐 الدالة تقبل فقط طلبات POST
def send_friendship_request(request, pk):
    try:
        # 👤 استرجاع بيانات المستخدم المستهدف
        user = User.objects.get(pk=pk)
        # 🔍 التحقق إذا كان هناك طلب صداقة مرسل أو مستلم
        send_request = FriendshipRequest.objects.filter(
            created_for=user, created_by=request.user
        ).first()
        received_request = FriendshipRequest.objects.filter(
            created_for=request.user, created_by=user
        ).first()
        # ✅ إذا لم يكن هناك أي طلبات صداقة موجودة
        if not send_request and not received_request:
            # ✉️ إنشاء طلب صداقة جديد
            FriendshipRequest.objects.create(
                created_for=user, created_by=request.user, status=FriendshipRequest.SEND
            )
            FriendshipRequest.objects.create(
                created_for=request.user,
                created_by=user,
                status=FriendshipRequest.WAITING,
            )
            return JsonResponse({"message": "Friendship request send successfully"})

        # ⚠️ إذا كان الطلب موجوداً بالفعل
        if send_request and send_request.status == FriendshipRequest.SEND:
            return JsonResponse({"message": "Request already send"})

        # 🔄 تحديث حالة الطلبات الحالية
        if send_request:
            send_request.status = FriendshipRequest.SEND
            send_request.save()

        if received_request:
            received_request.status = FriendshipRequest.WAITING
            received_request.save()

        # 💬 إرجاع رسالة النجاح
        return JsonResponse(
            {
                "message": "Friendship request updated successfully",
                "status": (
                    send_request.status if send_request else received_request.status
                ),
            }
        )

    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)
    except Exception as e:
        return JsonResponse(
            {"message": "An unexpected error occurred", "error": str(e)}, status=500
        )


# 🌐 واجهة برمجية لمعالجة وتحديث حالة طلب الصداقة
@api_view(["POST"])  # 🌐 الدالة تستقبل فقط طلبات POST
def handle_request(request, pk, status):
    try:
        # 🛠️ التحقق من إذن المستخدم
        if not request.user.is_authenticated:
            logger.warning("🚫 An unauthorized user has attempted to access.")
            raise PermissionDenied("You must be logged in to perform this action.")
        # 🧑‍🤝‍🧑 [ الصفحة اللى انا فيهاء ID الحصول على المستخدم المستهدف [اللى هو
        user = User.objects.get(pk=pk)
        # 🟢 افتراض أن المستخدم يمكنه إرسال طلب صداقة.
        can_send_friendship_request = True
        # 🔒 التحقق مما إذا كان المستخدم بالفعل صديقًا.
        if request.user in user.friends.all():
            can_send_friendship_request = False  # 🛑 لا يمكن إرسال طلب صداقة.

        # 🔍 🙏 [ صلاحيات المستخدم المرسل للطلب ] جلب طلب الصداقة المرسل
        friendship_request_send = FriendshipRequest.objects.filter(
            created_by=request.user, created_for=user
        ).first()
        # 🚫 🙏 [ صلاحيات المستخدم المرسل للطلب ] الغاء طلب الصداقة
        if friendship_request_send:
            # 💬 تحديث الحالة وتخزينها
            update_request_status(friendship_request_send, status)
            # 🚫 في حالة الإلغاء، تحديث المستخدم إلى حالة NOTSEND
            if status == "cancel":
                friendship_request_send.created_for.friendship_status = (
                    FriendshipRequest.NOTSEND
                )
                friendship_request_send.created_for.friendship_status = (
                    FriendshipRequest.CANCEL
                )
                friendship_request_send.created_for.save()
                logger.info(
                    f"🚫 The order has been cancelled and the user status has been restored. {user.name} To NOTSEND."
                )
        # _______________________________________
        # 🔍 🤝 [ صلاحيات المستخدم المستلم للطلب ] جلب طلب الصداقة المرسل
        friendship_request_waiting = FriendshipRequest.objects.filter(
            created_for=request.user, created_by=user
        ).first()
        # 🚫 🙏 [ صلاحيات المستخدم المرسل للطلب ] قبول او رفض طلب الصداقة
        if friendship_request_waiting:
            # 💬 تحديث الحالة وتخزينها
            update_request_status(friendship_request_waiting, status)
            # ✅ في حالة القبول، إضافة الأصدقاء
            if status == "accepted":
                add_friends(request.user, user)
                logger.info(f"✅ Added {request.user.name} And {user.name} As friends.")
            return JsonResponse(
                {
                    "message": f"Friendship request {status} successfully",
                    "status": status,
                }
            )
        # 🔴 ❌ [ صلاحيات المستخدم المرسل للطلب ] اذا حدث أخطاء
        if not friendship_request_waiting:
            logger.error(
                f"❌ Friendship request between {request.user.name} And {user.name} unavailable."
            )
            return JsonResponse({"error": "Friendship request not found"}, status=404)

    # _______________________________________
    except PermissionDenied as e:
        return JsonResponse({"error": str(e)}, status=403)
    except User.DoesNotExist:
        logger.error("❌ User not found.")
        return JsonResponse({"error": "User not found"}, status=404)
    except Exception as e:
        logger.exception("❌ An unexpected error occurred.")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)

    # 🟢 افتراض أن المستخدم يمكنه إرسال طلب صداقة.
    # can_send_friendship_request = True
    # # 🔒 التحقق مما إذا كان المستخدم بالفعل صديقًا.
    # if request.user in user.friends.all():
    #     can_send_friendship_request = False  # 🛑 لا يمكن إرسال طلب صداقة.
    #         "can_send_friendship_request": can_send_friendship_request,  # صلاحية إرسال طلب الصداقة.
    # # _____________________________________________
    # # _____________________________________________
    # # _____________________________________________
    # # _____________________________________________
    # # _____________________________________________


# 🛠️ وظيفة لتحديث حالة طلب الصداقة
def update_request_status(friendship_request, status):
    friendship_request.status = status
    friendship_request.save()
    logger.info(f"🔄 The order status has been updated to {status}.")

    # ❌ حذف الطلب في حالات معينة
    if status in [FriendshipRequest.WAITING, FriendshipRequest.SEND]:
        friendship_request.delete()
        logger.info(
            f"❌ The request was deleted between {friendship_request.created_by.username} And {friendship_request.created_for.username}."
        )


# 👫 وظيفة لإضافة الأصدقاء
def add_friends(user1, user2):
    user1.friends.add(user2)
    user1.friends_count += 1
    user1.save()

    user2.friends.add(user1)
    user2.friends_count += 1
    user2.save()


# 🌐 واجهة برمجية لاقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
@api_view(["GET"])  # 🌐 الدالة تقبل فقط طلبات GET
def my_friendship_suggestions(request):

    # 🤝 Suggest users the current user may know
    # 🤝 اقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
    # 🧑‍🤝‍🧑 السيريالايزر يقوم بتحويل قائمة المستخدمين الذين قد يعرفهم المستخدم إلى صيغة JSON
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)
    # print("🤝 Suggest users", serializer)

    # 📤 إرجاع البيانات كاستجابة JSON
    return JsonResponse(serializer.data, safe=False)
