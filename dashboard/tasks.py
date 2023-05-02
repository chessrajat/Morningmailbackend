import uuid
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from dashboard.models import Subscriber, SentEmail


def send_emails():
    print("Running send_emails.......")
    recipients = Subscriber.objects.values_list("email", flat=True)
    domain = "localhost:8000"
    for recipient in recipients:
        tracking_id = str(uuid.uuid4())
        subject = "Your Daily Tech News"
        html_message = render_to_string(
            "emailTemplate.html", {"tracking_id": tracking_id, "domain": domain})

        email = EmailMessage(
            subject=subject,
            body=html_message,
            to=[recipient],
        )
        email.content_subtype = 'html'
        sent = email.send()
        if sent == 1:
            print("Email sent successfully")
            is_successful = True
        else:
            print("Email sent failed")
            is_successful = False

        ee = SentEmail(
            recipient=Subscriber.objects.get(email=recipient),
            is_successful=is_successful,
            tracking_id=tracking_id
        )
        ee.save()
