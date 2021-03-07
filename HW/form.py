from django import forms
from django.forms import ModelForm
from .models import answer, homework
class creat_hw (ModelForm):
    class Meta :
        model= homework
        fields= '__all__'
class creat_answer (ModelForm):
    class Meta :
        model= answer
        fields=['ans_title', 'student_nu', 'ans_file']