from rest_framework import serializers
from .models import *

texts = "serializers.CharField serializers.ValidationError "

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
	messages = MessageSerializer(many=True, read_only=True)
	message_count = serializers.SerializerMethodField()

	class Meta:
		model = Conversation
		fields = '__all__'
	def get_message_count(self, obj):
		return obj.messages.count()