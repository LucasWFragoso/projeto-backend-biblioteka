from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler()


class LoanConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loan"

    def ready(self):
        from .jobs import LoanJob

        LoanJob.run()
        scheduler.start()
