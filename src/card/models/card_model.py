import uuid

from django.db import models


class Card(models.Model):
    card_uuid = models.UUIDField(default=uuid.uuid4)
    name = models.URLField()
