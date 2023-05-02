from django.apps import AppConfig
import threading

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        from .scheduler import scheduler
        scheduler.start()

