from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserDetail)
admin.site.register(LawyerDetail)
admin.site.register(ContactLawyer)
