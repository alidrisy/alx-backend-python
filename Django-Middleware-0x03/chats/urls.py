from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import (
    NestedDefaultRouter,
)
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r"chats/conversation", ConversationViewSet, basename="conversation")

nested_router = NestedDefaultRouter(
    router, r"chats/conversation", lookup="conversation"
)
nested_router.register(
    r"chats/conversation/messages", MessageViewSet, basename="conversation-messages"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_router.urls)),
]
