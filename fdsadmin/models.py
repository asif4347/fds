from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)

