from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
	role_choices = ('guest', 'host', 'admin')

	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
	password_hash = models.CharField(null=False, blank=False)
	phone_number = models.CharField(null=True)
	role = models.CharField(max_length=15, choices=role_choices, null=False, blank=False, default='guest')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name

class Message(models.Model):
	message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
	sender_id = models.ForeignKey(User)
	message_body = models.TextField(null=False, blank=False)
	sent_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message_body


# Conversation
#     conversation_id (Primary Key, UUID, Indexed)
#     participants_id (Foreign Key, references User(user_id)
#     created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

class Conversation(models.Model):
	conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
	participants_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

