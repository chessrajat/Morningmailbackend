from django.dispatch import receiver
from django.db.models.signals import post_save

from dashboard.models import Subscriber
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        subscriber = Subscriber.objects.create(email=email)
        subscriber.save()