from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PLAN_CHOICES = [
        ('free', 'Hollow (Free)'),
        ('pro', 'Lord of Cinder (Pro)'),
    ]
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')
    
    def __str__(self):
        return self.username