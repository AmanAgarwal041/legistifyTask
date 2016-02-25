from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,"home.html",{})

def signupuser(request):

    if form.is_valid():
        uname = form.cleaned_data.get("uname")
        email = form.cleaned_data.get("uname")
        pword = form.cleaned_data.get("pword")
        fname = form.cleaned_data.get("fname")
        pno = form.cleaned_data.get("pno")
        age = form.cleaned_data.get("age")
        gen = form.cleaned_data.get("gen")
        try:
            User.objects.create_user(username=uname, email=email, password=pword, first_name=fname, last_name='').save()
            UserDetail.objects.create(uid=uname, pno=pno, age=age, gen=gen)
        except:
            context = {
                        "error" : True
            }
            return render(request, "UserReg.html",context)
