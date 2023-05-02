import base64
from datetime import datetime, timedelta
from unittest.mock import sentinel
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

from dashboard.tasks import send_emails
from dashboard.models import SentEmail


class SendMails(APIView):
    def get(self, request, *args, **kwargs):
        try:
            send_emails()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DailyEmailStatsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            days = int(request.GET.get("days", 7))
        except Exception as e:
            print(e)
            print("here")
            days = 7
        today = timezone.now().date()
        start_date = today - timedelta(days=days-2)
        response_data = []
        for i in range(days):
            date = start_date + timedelta(days=i)
            todays_emails = SentEmail.objects.filter(sent_at__date=date)
            sent_count = todays_emails.filter(is_successful=True).count()
            failed_mail = todays_emails.filter(is_successful=False).count()
            opened_mails = todays_emails.filter(is_opened=True).count()
            response_data.append({
                "date": date,
                "sent": sent_count,
                "failed": failed_mail,
                "opened": opened_mails
            })
        return Response(response_data)


@csrf_exempt
def track_email(request, tracking_id):
    PIXEL_DATA = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mOUdOjBfQADvwGU0LY+5wAAAABJRU5ErkJggg=='
    try:
        email = SentEmail.objects.get(tracking_id=tracking_id)
        email.is_opened = True
        email.save()
    except SentEmail.DoesNotExist:
        pass

    # Return a transparent 1x1 pixel
    response = HttpResponse(content_type="image/gif")
    response.write(base64.b64decode(PIXEL_DATA))
    return response
