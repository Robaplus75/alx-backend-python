from rest_framework import viewsets, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

status = False
filters = False

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    permission_classes = [permissions.AllowAny]

class MessageViewSet(viewsets.ModelViewSet):
	serializer_class = MessageSerializer
	queryset = Message.objects.all()
	permission_classes = [permissions.AllowAny]
