from django.db import models
from django.utils import timezone

class Photo(models.Model):
    key = models.CharField(max_length=150)
    is_approve = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.key

    def approved(self):
    	return self.is_approve