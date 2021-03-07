from django import forms
from django.forms import ModelForm
from .models import teachvideos
class creat_vid (ModelForm):
    class Meta :
        model= teachvideos
        fields= '__all__'