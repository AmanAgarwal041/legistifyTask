from django.contrib import admin

# Register your models here.
from .models import *

class UserDetailAdmin (admin.ModelAdmin):
    list_display = ["__unicode__", "pno", "gen", "age"]
    class Meta:
        model = UserDetail

class LawyerDetailAdmin (admin.ModelAdmin):
    list_display = ['lid', 'pno', 'age', 'gen', 'experience', 'speciality']
    class Meta:
        model = LawyerDetail

class ContactLawyerAdmin (admin.ModelAdmin):
    list_display = ['contact_id', 'uid', 'lid', 'status']
    class Meta:
        model = ContactLawyer

admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(LawyerDetail, LawyerDetailAdmin)
admin.site.register(ContactLawyer, ContactLawyerAdmin)
