import uuid

from django.db import models
from mailinglist.models import MailingList


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False),
    mailing_list = models.ForeignKey(to=MailingList, on_delete=models.CASCADE),
    subject = models.CharField(max_length=140),
    body = models.TextField()
    started = models.DateTimeField(default=None, null=True),
    finished = models.DateTimeField(default=None, null=True)
