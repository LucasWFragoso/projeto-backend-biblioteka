from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime
from apscheduler.job import Job
from django.contrib.auth import get_user_model

# import logging

# logging.basicConfig()
# logging.getLogger("apscheduler").setLevel(logging.DEBUG)
scheduler = BackgroundScheduler()

User = get_user_model()


def block_user(user_id):
    user = User.objects.get(id=user_id)
    user.is_allowed = False
    user.save()


class LoanJob(Job):
    @staticmethod
    def run():
        from .models import Loan

        print(datetime.now())
        loans = Loan.objects.filter(is_returned=False, devolution_date__lt=date.today())
        for loan in loans:
            block_user(loan.user_id)
            loan.save()

    # def job():

    # scheduler = BackgroundScheduler()
    # scheduler.add_job(job, "interval", seconds=60)
    # scheduler.start()


scheduler.add_job(
    LoanJob.run,
    trigger="interval",
    minutes=1,
    id="loan_check",
    replace_existing=True,
)
