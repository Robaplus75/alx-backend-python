from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """
        Returns unread message
        """
        return self.filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')
