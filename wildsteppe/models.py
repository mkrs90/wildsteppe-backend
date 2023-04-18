from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.username

class Activity(models.Model):
    name = models.CharField(max_length=50)

    