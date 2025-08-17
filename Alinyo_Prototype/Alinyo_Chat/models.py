import uuid
from django.db import models

class Messages(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.UUIDField("Session ID", default=uuid.uuid4, editable=False)
