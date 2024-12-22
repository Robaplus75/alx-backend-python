from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
	role_choices = (('guest', 'guest'), ('host','host'), ('admin','admin'))

	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
	first_name = models.CharField(max_length=255, null=False, blank=False)
	last_name = models.CharField(max_length=255, null=False, blank=False)
	email = models.EmailField(unique=True, null=False, blank=False)
	password_hash = models.CharField(max_length=100, null=False, blank=False)
	phone_number = models.CharField(max_length=100, null=True)
	role = models.CharField(max_length=15, choices=role_choices, null=False, blank=False, default='guest')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name

class Message(models.Model):
	message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
	sender_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	message_body = models.TextField(null=False, blank=False)
	sent_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message_body

class Conversation(models.Model):
	conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
	participants_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)

