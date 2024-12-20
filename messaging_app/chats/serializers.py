from django_restframework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Message
		fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Conversation
		fields = '__all__'