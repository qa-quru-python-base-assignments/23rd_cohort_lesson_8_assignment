from pathlib import Path

from src.email import Email
from src.email_address import EmailAddress
from src.email_service import EmailService
from src.status import Status


class LoggingEmailService(EmailService):
    def send_email(self) -> list[Email]:
        sent_emails = super().send_email()
        if sent_emails:
            self._log_to_file(sent_emails)

        return sent_emails

    @staticmethod
    def _log_to_file(emails: list[Email]):
        with open(Path(__file__).parent.parent / "send.log", "w", encoding="utf-8") as logfile:
            print(*emails, sep="\n====================\n", file=logfile)


# LoggingEmailService Demo
if __name__ == '__main__':
    email = Email(
        subject="T",
        body="B",
        sender=EmailAddress("a@a.com"),
        recipients=[EmailAddress("b@b.com"), EmailAddress("c@c.com")],
        status=Status.READY,
    )
    service = LoggingEmailService(email)
    service.send_email()
