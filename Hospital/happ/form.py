from django import forms
from .models import patient

class appointment(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['name','email','phone','doctor','department']