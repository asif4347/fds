from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    area_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.area_name


class Volenteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(default='Voleenteer', blank=False, max_length=10)
    address = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False)
    pick_locations=models.ManyToManyField(Location)


    def __str__(self):
        return self.name