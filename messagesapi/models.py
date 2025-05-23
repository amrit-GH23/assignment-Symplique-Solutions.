# models.py
from django.db import models

class Message(models.Model):
    date = models.DateField()
    time = models.TimeField()
    content = models.TextField()

    def __str__(self):
        return f"{self.date} {self.time}: {self.content[:50]}"
