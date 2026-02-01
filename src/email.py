import re
import textwrap
from dataclasses import dataclass
from datetime import datetime

from src.email_address import EmailAddress
from src.status import Status


@dataclass
class Email:
    subject: str
    body: str
    sender: EmailAddress
    recipients: EmailAddress | list[EmailAddress]
    short_body: None | str = None
    date: None | datetime = None
    status: Status = Status.DRAFT

    def __post_init__(self):
        if isinstance(self.recipients, EmailAddress):
            self.recipients = [self.recipients]

    def __repr__(self):
        content = f"""
            Status: {self.status}
            Кому: {self.get_recipients_str()}
            От: {self.sender.masked}
            Тема: {self.subject}, дата {self.date:%d.%m.%Y %H:%M}
            {self.short_body or self.body}
        """
        return textwrap.dedent(content).strip()

    @staticmethod
    def __normalize_text(text: str):
        return re.sub(r"[\n\t ]+", " ", text.strip())

    def __normalize_subject(self):
        self.subject = self.__normalize_text(self.subject)

    def __normalize_body(self):
        self.body = self.__normalize_text(self.body)

    def __set_status(self):
        if self.subject and self.body and self.sender and self.recipients:
            self.status = Status.READY
        else:
            self.status = Status.INVALID

    def get_recipients_str(self):
        return ", ".join([recipient.masked for recipient in self.recipients])

    def add_short_body(self, n: int = 10):
        if not self.body:
            self.short_body = None
            return

        suffix = "..." if len(self.body) > n else ""
        self.short_body = f"{self.body[:n]}{suffix}"

    def prepare(self):
        self.__normalize_subject()
        self.__normalize_body()
        self.__set_status()
        self.add_short_body()
        return self
