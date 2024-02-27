from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to our site!'
        message = 'Dear {},\n\nThank you for registering on our site.'.format(instance.email)
        sender_email = settings.DEFAULT_FROM_EMAIL
        recipient_email = instance.email
        send_mail(subject, message, sender_email, [recipient_email])
