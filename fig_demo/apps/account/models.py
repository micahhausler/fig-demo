from django.db import models

from json_field import JSONField
from uuidfield import UUIDField


class Account(models.Model):

    user = models.OneToOneField('auth.User')
    metadata = JSONField(null=False, blank=True, default=lambda: {})
    uuid = UUIDField(auto=True)
