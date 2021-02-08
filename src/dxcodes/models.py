from django.db import models
from datetime import datetime
from categories.models import Category

class Dxcode(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    diagnosis_code = models.CharField(max_length=20, unique=True)
    full_code = models.CharField(max_length=20, unique=True)
    abbreviated_description = models.TextField(max_length=150)
    full_description = models.TextField(max_length=200)
    category_title = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):

        return self.full_description



