# chats/views.py

from rest_framework import generics
from .serializers import MessageSerializer
from .filters import MessageFilter
from .pagination import MessagePagination
from .permissions import IsParticipantOfConversation
from django_filters.rest_framework import DjangoFilterBackend

class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = MessagePagination
    permission_classes = [IsParticipantOfConversation]
