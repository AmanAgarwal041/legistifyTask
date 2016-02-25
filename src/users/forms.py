from django import forms
from .models import *

class SignUpUserForm (forms.ModelForm):
    class Meta:
        model = UserDetail
        exclude = []

class SignUpLawyerForm (forms.ModelForm):
    class Meta:
        model = LawyerDetail
        exclude = []
