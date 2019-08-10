import datetime
from django import forms
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
from django.db import models
from .models import *

class PermForm(ModelForm):

    class Meta:
        model = Permissionform
        fields = ('club','building','room','purpose','dates')

    def clean(self):
        cleaned_data = super(PermForm, self).clean()
        date = cleaned_data.get('dates')
        if date <= date.today():
            raise forms.ValidationError("The date entered has passed")

        build = cleaned_data.get('building')
        room = cleaned_data.get('room')
        flag = 0
        for each in Building.objects.all():
            if str(build) == str(each.name):
                for per in each.room_set.all():
                    if str(per.number) == str(room):
                        flag = 1
        if flag == 0:
            raise forms.ValidationError("The selected room is not in the selected building")
