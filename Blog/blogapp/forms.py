from django import forms
from .models import blog

class editForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['name','desc']