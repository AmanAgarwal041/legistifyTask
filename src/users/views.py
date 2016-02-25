from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,"home.html",{})

def signupuser(request):
    form = SignUpUserForm(request.POST or None)
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
            UserDetail.objects.create(uid=uname, pno=pno, age=age, gen=gen).save()
            return render(request, "login.html",{})
        except:
            context = {
                        "error" : True
            }
            return render(request, "UserReg.html",context)
    else:
        return render(request, "UserReg.html",{})

def signuplawyer(request):
    form = SignUpLawyerForm(request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data.get("uname")
        email = form.cleaned_data.get("uname")
        pword = form.cleaned_data.get("pword")
        fname = form.cleaned_data.get("fname")
        pno = form.cleaned_data.get("pno")
        age = form.cleaned_data.get("age")
        gen = form.cleaned_data.get("gen")
        speciality = form.cleaned_data.get("speciality")
        experience = form.cleaned_data.get("experience")
        try:
            User.objects.create_user(username=uname, email=email, password=pword, first_name=fname, last_name='').save()
            LawyerDetail.objects.create(uid=uname, pno=pno, age=age, gen=gen, speciality=speciality, experience=experience).save()
            return render(request, "login.html",{})
        except:
            context = {
                        "error" : True
            }
            return render(request, "LawyerReg.html",context)
    else:
        return render(request, "LawyerReg.html", {})


def login(request):
    if request.user.is_authenticated():
        if request.POST:
            uname = request.POST['uname']
            pword = request.POST['pword']
            user = auth.authenticate(username=uname, password=pword)
            if user is not None and user.is_active:
                auth.login(request, user)
                usergetdetails = UserDetail.objects.get(uid=uname)
                lawyergetdetails = LawyerDetail.objects.get(uid=uname)
                if usergetdetails is not None and lawyergetdetails is None:
                    return render(request, "UserDashboard.html",{})
                elif usergetdetails is None and lawyergetdetails is not None:
                    return render(request, "LawyerDashboard.html",{})

        else:
            return render(request,"login.html",{})
