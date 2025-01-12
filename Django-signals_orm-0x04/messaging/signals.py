from django.db.models.signals import pre_save, post_save, post_delete
from .models import Message, MessageHistory, Notification
from django.dispatch import receiver

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """
    Automatically creates a notification for the receiver when a new message is sent.
    """
    if created:  # Ensure this runs only when a new message is created
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(post_delete, sender=User)
def clean_up_user_data(sender, instance, **kwargs):
    """
    Deletes all related stuff when a user is deleted.
    """
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(edited_by=instance).delete()

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """
    Logs the old content of a message into the MessageHistory model before it is updated.
    """
    if instance.pk:  
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
                MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content
            ) 
            instance.edited = True

