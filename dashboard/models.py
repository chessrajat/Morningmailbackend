from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class SentEmail(models.Model):
    recipient = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name="sent_emails")
    sent_at = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)
    is_opened = models.BooleanField(default=False)
    tracking_id = models.UUIDField(unique=True)

    def __str__(self) -> str:
        return str(self.tracking_id)
