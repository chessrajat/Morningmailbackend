from django.contrib import admin

from dashboard.models import Subscriber, SentEmail

admin.site.register((Subscriber, SentEmail))
