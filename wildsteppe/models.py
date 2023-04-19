from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    def __str__(self):
        return str(self.email)

    class Meta(AbstractUser.Meta):
        ordering = ["-date_joined"]
        db_table = "users"

# class CustomUser(AbstractUser):
#     birthday = models.DateField(null=True)

#     def __str__(self):
#         return self.username

class Activity(models.Model):
    name = models.CharField(max_length=50)

class Trail(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True)
    distance = models.FloatField()
    duration = models.IntegerField()
    image = models.URLField(null=True)
    pets_allowed = models.BooleanField()
    