from django.db import models
from django.utils import timezone
import uuid 

class Photo(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.key)