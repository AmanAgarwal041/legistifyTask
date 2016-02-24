from django.shortcuts import render
from .forms import LoginForm
# Create your views here.

def home(request):
    title = "Welcome All"
    if request.user.is_authenticated():
        title = "Welcome %s" %(request.user)

    form = LoginForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=True)
        print instance


    context = {
        "title_temp" : title,
        "form" : form
    }
    return render(request, "home.html", context)
