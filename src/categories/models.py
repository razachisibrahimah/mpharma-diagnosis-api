from django.db import models
from datetime import datetime


class Category(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title