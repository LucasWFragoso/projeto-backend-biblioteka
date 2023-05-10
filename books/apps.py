from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler()


class BooksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "books"

    def ready(self):
        from .jobs import BookJob

        scheduler.add_job(
            BookJob.run,
            trigger="interval",
            hours=120,
            id="loan_check",
            replace_existing=True,
        )
        scheduler.start()
