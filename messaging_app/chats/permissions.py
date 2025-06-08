from rest_framework import permissions
from .models import Conversation


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of a message/conversation to view or edit it.
    Admins have full access.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if hasattr(obj, "user"):
            return obj.user == request.user

        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()

        return False


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """
    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant in the conversation
        if isinstance(obj, Conversation):
            return request.user in [obj.sender, obj.recipient]
        # For Message objects, check if user is part of the conversation
        return request.user in [obj.conversation.sender, obj.conversation.recipient]
