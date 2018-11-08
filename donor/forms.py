from django.forms import ModelForm,models
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model=Donor
        fields=(
            "name",
            "address",
            'city',
            'country',
            "mobile",
            "area_name",
            'gender',
            'image'

        )

class FoodForm(ModelForm):
    class Meta:
        model=Food
        fields=(
            "food_title",
            "food_type",
            "preparation_date",
            "post_date",
            "quantity",
            'image'
        )

class FeedbackForm(ModelForm):
    class Meta:
       model = Feedback
       fields = (
                    'full_name',
                    'email',
                    'comment',
                )

