import datetime
from django import forms
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from .models import *

class PermForm(ModelForm):
    class Meta:
        model = Permissionform
        fields = ('club','building','room','purpose','dates')
        widgets = {
            'purpose': Textarea(attrs={'rows': 5}),
            }

    def clean(self):
        cleaned_data = super(PermForm, self).clean()
        date = cleaned_data.get('dates')
        if date <= date.today():
            raise forms.ValidationError("The date entered has passed")
