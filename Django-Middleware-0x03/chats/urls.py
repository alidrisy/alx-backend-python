from django.urls import path, include  # ✅ استيراد path و include
from rest_framework import routers  # ✅ استيراد DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter  # ✅ في حال استخدام الراوتر المتداخل
from .views import ConversationViewSet, MessageViewSet

# الراوتر الرئيسي
router = routers.DefaultRouter()
router.register(r"conversations", ConversationViewSet, basename="conversation")  # ✅ conversations

# الراوتر المتداخل للرسائل ضمن المحادثات
nested_router = NestedDefaultRouter(router, r"conversations", lookup="conversation")
nested_router.register(r"messages", MessageViewSet, basename="conversation-messages")  # ✅ nested messages

urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_router.urls)),  # ✅ تضمين الراوتر المتداخل
]
