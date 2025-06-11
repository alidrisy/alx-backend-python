import django_filters
from .models import Message, Conversation

class MessageFilter(django_filters.FilterSet):
    """
    Filter class for Message model
    Allows filtering by:
    - sender: Filter by message sender
    - conversation: Filter by specific conversation
    - created_at: Filter by creation date (exact, greater than, less than)
    - content: Filter by message content (case-insensitive contains)
    """
    sender = django_filters.CharFilter(field_name='sender__username')
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'created_at_after', 'created_at_before', 'content']

class ConversationFilter(django_filters.FilterSet):
    """
    Filter class for Conversation model
    Allows filtering by:
    - participant: Filter by conversation participant
    - created_at: Filter by creation date
    """
    participant = django_filters.CharFilter(field_name='participants__username')
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Conversation
        fields = ['participant', 'created_at_after', 'created_at_before'] 