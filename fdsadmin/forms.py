from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model=FdsAdmin
        fields=(
            "name",
            "cnic",
            "address",
            'city',
            'country',
            "mobile",
            'gender',
            'image',

        )
