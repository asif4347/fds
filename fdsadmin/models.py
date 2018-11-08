from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)


class Rating(models.Model):
    rate=models.IntegerField(null=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
