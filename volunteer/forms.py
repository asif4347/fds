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