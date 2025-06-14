from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Message, MessageHistory, Notification


@receiver(pre_save, sender=Message)
def save_old_content_to_history(sender, instance, **kwargs):
    if instance.pk:
        try:
            old = Message.objects.get(pk=instance.pk)
            if old.content != instance.content:
                MessageHistory.objects.create(
                    message=old,
                    old_content=old.content,
                    changed_by=instance.edited_by,  # يجب تمريره من view
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass


@receiver(post_save, sender=Message)
def create_notification_on_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)
