from django import forms
from django.utils.safestring import mark_safe


from django.forms import ModelForm
from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ()
