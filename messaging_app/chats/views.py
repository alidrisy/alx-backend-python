from rest_framework import viewsets, permissions
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from django.shortcuts import get_object_or_404


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Create a new conversation with participants
        conversation = serializer.save()
        user_ids = self.request.data.get("participant_ids", [])
        users = User.objects.filter(user_id__in=user_ids)
        conversation.participants.set(users)
        conversation.save()

    def get_queryset(self):
        # Only return conversations the user is part of
        return Conversation.objects.filter(participants=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Send a message in an existing conversation
        conversation_id = self.request.data.get("conversation_id")
        conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
        serializer.save(sender=self.request.user, conversation=conversation)

    def get_queryset(self):
        # Only messages in conversations the user is part of
        return Message.objects.filter(conversation__participants=self.request.user)
