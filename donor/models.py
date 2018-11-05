from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now
# Create your models here.

gender={
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")

}
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(default='Donor',blank=False,max_length=10)
    address = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False)
    area_name=models.CharField(help_text='Johar Town, Faisal Town',max_length=30)
    image=models.ImageField(blank=True)
    gender=models.CharField(max_length=6,blank=True,null=True,choices=gender)
    city=models.CharField(max_length=20,blank=True,null=True)
    country=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name

choices={
    ("New Entry","New Entry"),
    ("Picked","Picked"),
    ("Delivered","Delivered")
}
food_types={
    ("Fast Food","Fast Food"),
    ("Regular Food","Regular Food"),
}

class Food(models.Model):
    donor=models.ManyToManyField(Donor)
    food_title=models.CharField(max_length=15,null=False,blank=False,)
    food_type = models.CharField(max_length=15, null=False, blank=False, choices=food_types)
    quantity=models.IntegerField(blank=False)
    delivered_at = models.CharField(max_length=50, default="NAN")
    preparation_date=models.DateField(blank=True,default=now())
    post_date = models.DateField(blank=True, default=now())
    status=models.CharField(choices=choices,max_length=10,default='New Entry')
    location=models.CharField(max_length=200,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.food_type


class Feedback(models.Model):
    full_name=models.CharField(max_length=15, null=False, blank=False)
    email=models.CharField(max_length=20, null=False, blank=False)
    comment=models.CharField(max_length=500, null=False, blank=False)
