from django.forms import ModelForm,models
from .models import *


class ProfileForm(ModelForm):
    password1=models.CharField(max_length=50,type='password')
    password2=models.CharField(max_length=50,type='password')
    class Meta:
        model=Donor
        fields=(
            "name",
            "address",
            "mobile",
            "area_name",
            "password1",
            "password2",
        )