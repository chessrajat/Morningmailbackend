from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone

from dashboard.tasks import send_emails

scheduler = BackgroundScheduler(timezone=timezone.get_current_timezone())
scheduler.add_jobstore(DjangoJobStore(), "default")



scheduler.add_job(send_emails, "cron", hour=10, minute=0)