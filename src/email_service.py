from datetime import datetime

from src.email import Email
from src.status import Status


class EmailService:
    def __init__(self, email: Email):
        self.email = email

    def send_email(self) -> list[Email]:
        sent_emails = []
        for recipient in self.email.recipients:
            sent_emails.append(
                Email(
                    subject=self.email.subject,
                    body=self.email.body,
                    sender=self.email.sender,
                    recipients=recipient,
                    short_body=self.email.short_body if self.email.short_body else self.email.add_short_body(),
                    date=datetime.now(),
                    status=Status.SENT if self.email.status == Status.READY else Status.FAILED
                )
            )
        return sent_emails
