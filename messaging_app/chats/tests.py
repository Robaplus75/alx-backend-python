
from django.test import TestCase
from .models import User, Message, Conversation

class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User ',
            email='testuser@example.com',
            password='password123'
        )

    def test_user_creation(self):
        """Test that a user is created successfully."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User ')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.role, 'guest')  # Default role

    def test_user_str(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), 'Test')

class MessageModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User ',
            email='testuser@example.com',
            password='password123'
        )
        self.message = Message.objects.create(
            sender_id=self.user,
            message_body='Hello, this is a test message.'
        )

    def test_message_creation(self):
        """Test that a message is created successfully."""
        self.assertEqual(self.message.sender_id, self.user)
        self.assertEqual(self.message.message_body, 'Hello, this is a test message.')

    def test_message_str(self):
        """Test the string representation of the message."""
        self.assertEqual(str(self.message), 'Hello, this is a test message.')

class ConversationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User ',
            email='testuser@example.com',
            password='password123'
        )
        self.conversation = Conversation.objects.create(
            participants_id=self.user
        )

    def test_conversation_creation(self):
        """Test that a conversation is created successfully."""
        self.assertEqual(self.conversation.participants_id, self.user)

    def test_conversation_str(self):
        """Test the string representation of the conversation."""
        self.assertEqual(str(self.conversation), str(self.conversation.conversation_id))  # Adjust as needed
