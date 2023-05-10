from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime
from apscheduler.job import Job
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .models import Follow, Book
import os
import dotenv


def send_emails():
    books = Book.objects.filter(copies_count__gt=0)
    emails = []
    for book in books:
        follows = Follow.objects.filter(book_id=book.id)
        for follow in follows:
            emails.append(follow.user.email)
        send_mail(
            subject=f"Notícias sobre o livro {book.name} que você segue!",
            message=f"Oba! o livro {book.name} que você segue está disponível para ser emprestado.",
            from_email=os.getenv("EMAIL_HOST_USER"),
            recipient_list=emails,
            fail_silently=False,
        )


class BookJob(Job):
    @staticmethod
    def run():
        send_emails()
