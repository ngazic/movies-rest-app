from django.core.mail import EmailMessage
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(subject, to:list,body):
        email = EmailMessage(
            subject=subject, body=body, to=to)
        EmailThread(email).start()
