from django import forms
from .models import Choice, Question
from django.contrib.auth.models import User

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']