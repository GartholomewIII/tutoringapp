from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    subjects = models.JSONField(default=list, blank=True)
    days = models.JSONField(default=list, blank=True)
    hours = models.JSONField(default=list, blank=True)