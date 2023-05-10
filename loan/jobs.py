from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime
from apscheduler.job import Job
from django.contrib.auth import get_user_model


User = get_user_model()


def block_user(user_id):
    user = User.objects.get(id=user_id)
    user.is_allowed = False
    user.save()


class LoanJob(Job):
    @staticmethod
    def run():
        from .models import Loan

        loans = Loan.objects.filter(is_returned=False, devolution_date__lt=date.today())
        for loan in loans:
            block_user(loan.user_id)
            loan.save()
