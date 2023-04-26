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

class Activity(models.Model):
    name = models.CharField(max_length=50)

class Difficulty(models.Model):
    name = models.CharField(max_length=50)

class Comment(models.Model):
    text = models.TextField(max_length=250)
    stars = models.IntegerField(null=True)
    date = models.DateTimeField()
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    trail = models.ForeignKey('Trail', on_delete=models.PROTECT)

class Trail(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True)
    distance = models.FloatField()
    duration = models.IntegerField()
    image = models.URLField(null=True)
    pets_allowed = models.BooleanField()
    difficulty = models.ForeignKey('Difficulty', on_delete=models.PROTECT, null=True)
    activities = models.ManyToManyField('Activity', help_text="Select Activity")



    