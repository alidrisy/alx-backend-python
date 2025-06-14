from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        logout(request)  # تسجيل الخروج قبل الحذف
        user.delete()
        messages.success(request, "تم حذف حسابك بنجاح.")
        return redirect("home")  # غيّر هذا إلى اسم صفحتك الرئيسية
    return redirect("profile")  # إذا جاء المستخدم عبر GET
