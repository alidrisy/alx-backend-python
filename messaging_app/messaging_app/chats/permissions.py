from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a message/conversation to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        return obj.user == request.user

class IsConversationParticipant(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to view or modify it.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant in the conversation
        return request.user in [obj.user1, obj.user2] 