from datetime import datetime

from django.db import models


class Page(models.Model):
    """
    A record of pages
    """
    url = models.URLField(max_length=512)
    response = models.TextField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)
    called_time = models.DateTimeField(null=True, blank=True)

    def record_call(self, response, status_code):
        self.called_time = datetime.utcnow()
        self.response = response
        self.status_code = status_code
        self.save()

    def clear_call(self):
        self.called_time = None
        self.response = None
        self.status_code = None
        self.save()
