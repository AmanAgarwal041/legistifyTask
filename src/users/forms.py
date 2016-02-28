from django import forms
from .models import *

class SignUpUserForm (forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ["uid","pno","age", "gen"]

class SignUpLawyerForm (forms.ModelForm):
    class Meta:
        model = LawyerDetail
        fields = ["lid","pno","age", "gen","experience","speciality"]

class ContactLawyerForm (forms.ModelForm):
    class Meta:
        model = ContactLawyer
        fields = ["contact_id","uid","lid","status"]
