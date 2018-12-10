from django.forms import ModelForm, models, Textarea
from django import forms

from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Donor
        fields = (
            "name",
            "cnic",
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
        model = Food
        fields = (
            "food_title",
            "food_type",
            "preparation_date",
            "post_date",
            "quantity",

        )


class FeedbackForm(ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback

        fields = (
            'full_name',
            'email',
            'comment',
        )
