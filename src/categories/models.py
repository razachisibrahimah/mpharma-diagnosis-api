from django.db import models
from datetime import datetime
from django.urls import reverse




class Category(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return '%s, %s' % (self.code, self.title)

        # return self.title