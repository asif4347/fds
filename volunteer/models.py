from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Location(models.Model):
    area_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.area_name


gender = {
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")

}


class Volenteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(default='Voleenteer', blank=False, max_length=10)
    address = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False)
    pick_locations = models.ManyToManyField(Location,help_text="press ctrl and click to select multiple")
    image = models.ImageField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=gender)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    cnic = models.CharField(max_length=15, blank=True, null=True)
    code=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.name
