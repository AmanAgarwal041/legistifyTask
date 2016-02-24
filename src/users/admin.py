from django.contrib import admin

# Register your models here.
from .forms import LoginForm
from .models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "pword", "utype"]
    form = LoginForm
    class Meta:
        model = Login

admin.site.register(Login, LoginAdmin)
