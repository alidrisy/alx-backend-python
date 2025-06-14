from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.cache import cache_page


@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "تم حذف حسابك بنجاح.")
        return redirect("home")
    return redirect("profile")


@login_required
def user_messages_threaded(request):
    messages = (
        Message.objects.filter(sender=request.user)
        .select_related("sender", "receiver")
        .prefetch_related("replies")
    )

    messages = (
        Message.objects.filter(sender=request.user)
        .select_related("sender", "receiver")
        .prefetch_related("replies")
    )

    messages = messages.filter(parent_message__isnull=True)

    def get_thread(message):
        replies = message.replies.select_related("sender").all()
        return {"message": message, "replies": [get_thread(reply) for reply in replies]}

    threaded_messages = [get_thread(msg) for msg in messages]

    return render(
        request,
        "messaging/threaded_messages.html",
        {
            "threaded_messages": threaded_messages,
        },
    )


@cache_page(60)
@login_required
def unread_messages_view(request):
    unread_messages = (
        Message.unread.unread_for_user(request.user)
        .select_related("sender")
        .only("id", "sender__username", "content", "sent_at")
    )
    return render(
        request,
        "messaging/unread_messages.html",
        {
            "unread_messages": unread_messages,
        },
    )
