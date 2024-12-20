from django_restframework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
	messages = MessageSerializer(many=True, read_only=True)  # Assuming a related_name for messages
    message_count = serializers.SerializerMethodField()  # Example of using SerializerMethodField

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'start_time', 'message_count']

    def get_message_count(self, obj):
        return obj.messages.count()  # Assuming messages is a related name for the Message model