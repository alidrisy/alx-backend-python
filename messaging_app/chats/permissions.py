from rest_framework import permissions
from .models import Conversation, Message


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
    Different methods have different permission requirements:
    - GET: Must be a participant to view
    - POST: Must be a participant to send messages
    - PUT/PATCH: Must be the sender of the message to update
    - DELETE: Must be the sender of the message or a participant with delete rights
    """
    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # First check if user is a participant
        if isinstance(obj, Conversation):
            is_participant = request.user in [obj.sender, obj.recipient]
        else:  # Message object
            is_participant = request.user in [obj.conversation.sender, obj.conversation.recipient]

        if not is_participant:
            return False

        # For GET requests, being a participant is enough
        if request.method in permissions.SAFE_METHODS:
            return True

        # For PUT, PATCH, DELETE requests on messages
        if isinstance(obj, Message):
            if request.method in ['PUT', 'PATCH']:
                # Only the sender can modify their own messages
                return obj.sender == request.user
            elif request.method == 'DELETE':
                # Sender can delete their own messages
                # or participants can delete messages in their conversations
                return obj.sender == request.user or is_participant

        # For conversations, participants can perform all actions
        return is_participant
