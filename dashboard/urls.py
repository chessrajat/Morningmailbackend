
from django.urls import path

from dashboard.views import SendMails, track_email, DailyEmailStatsView


urlpatterns = [
    path("sendmails/", SendMails.as_view()),
    path("track/<str:tracking_id>/", track_email),
    path("dailystats/", DailyEmailStatsView.as_view())
]
