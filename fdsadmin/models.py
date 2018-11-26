from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from volunteer.models import gender

class Contact(models.Model):
    full_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)


class Rating(models.Model):
    rate=models.IntegerField(null=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __int__(self):
        return self.rate


class FdsAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(default='Admin', blank=False, max_length=10)
    address = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False)
    image = models.ImageField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=gender)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    cnic = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name