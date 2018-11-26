from django.forms import ModelForm
from .models import Volenteer,Location
from donor.models import Food


class FoodSaveForm(ModelForm):
    class Meta:
        model=Food
        fields=(
            'status',
            'delivered_at'
        )


class ProfileForm(ModelForm):
    class Meta:
        model=Volenteer
        fields=(
            "name",
            "cnic",
            "address",
            'city',
            'country',
            "mobile",
            'gender',
            'pick_locations',
            'image',

        )
