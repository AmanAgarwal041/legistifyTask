from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"home.html",{})

def signupuser(request):
	if request.session['type']:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/home/')
	else:
		if request.POST:
			uname = request.POST["uname"]
			email = request.POST["email"]
			pword = request.POST["pword"]
			cpword = request.POST["cpword"]
			fname = request.POST["fname"]
			pno = request.POST["pno"]
			age = request.POST["age"]
			gen = request.POST["gen"]
			try:
				email_reg = User.objects.get(email=email)
			except:
				email_reg = None
			if email_reg is not None:
				context = {
							"error" : True,
							"error_message": "Email Already Registered!"
				}
				return render(request, "UserReg.html",context)
			elif pword != cpword:
				context = {
							"error" : True,
							"error_message": "Password do not match!"
				}
				return render(request, "UserReg.html",context)
			else:
				try:
					user = User.objects.create_user(username=uname, email=email, password=pword, first_name=fname, last_name='')
					user.save()
					UserDetail.objects.create(uid=uname, pno=pno, age=age, gen=gen).save()
					return redirect('/login/')
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					context = {
								"error" : True,
								"error_message":e.message
					}
					return render(request, "UserReg.html",context)
		else:
			return render(request, "UserReg.html",{})

def signuplawyer(request):
	if request.session['type']:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/home/')
	else:
		if request.POST:
			uname = request.POST["uname"]
			email = request.POST["email"]
			pword = request.POST["pword"]
			cpword = request.POST["cpword"]
			fname = request.POST["fname"]
			pno = request.POST["pno"]
			age = request.POST["age"]
			gen = request.POST["gen"]
			speciality = request.POST["speciality"]
			experience = request.POST["experience"]
			try:
				email_reg = User.objects.get(email=email)
			except:
				email_reg = None
			if email_reg is not None:
				context = {
							"error" : True,
							"error_message": "Email Already Registered!"
				}
				return render(request, "LawyerReg.html",context)
			elif pword != cpword:
				context = {
							"error" : True,
							"error_message": "Password do not match!"
				}
				return render(request, "LawyerReg.html",context)
			else:
				try:
					user = User.objects.create_user(username=uname, email=email, password=pword, first_name=fname, last_name='')
					user.save()
					LawyerDetail.objects.create(lid=uname, pno=pno, age=age, gen=gen, speciality=speciality, experience=experience).save()
					return redirect('/login/')
				except Exception as e:
					print '%s (%s)' % (e.message, type(e))
					context = {
								"error" : True,
								"error_message":e.message
					}
					return render(request, "LawyerReg.html",context)
		else:
			return render(request, "LawyerReg.html", {})


def login(request):
	if request.session['type']:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/home/')
	else:
		if request.POST:
			uname = request.POST['uname']
			pword = request.POST['pword']
			try:
				user = auth.authenticate(username=uname, password=pword)
			except:
				user = None
			if user is not None:
				try:
					usergetdetails = UserDetail.objects.get(uid=uname)
				except:
					usergetdetails = None
				try:
					lawyergetdetails = LawyerDetail.objects.get(lid=uname)
				except:
					lawyergetdetails = None
				if usergetdetails is not None and lawyergetdetails is None:
					auth.login(request,user)
					request.session['type'] = "user"
					return redirect('/userdashboard/')
				elif usergetdetails is None and lawyergetdetails is not None:
					auth.login(request,user)
					request.session['type'] = "lawyer"
					return redirect('/lawyerdashboard/')
				else:
					context = {
								"error" : True,
								"error_message":"No such user registered!"
					}
					return render(request, "login.html",context)
			else:
				context ={
					"error" : True,
					"error_message":"Either Username or Password is wrong!"
				}
				return render(request, "login.html",{})
		else:
			return render(request,"login.html",{})


def userdashboard(request):
	if request.session['type']:
		if request.session['type']=='user':
			return render(request, "UserDashboard.html", {})
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/home/')
	else:
		return redirect('/home/')

def lawyerdashboard(request):
	if request.session['type']:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return render(request, "LawyerDashboard.html", {})
		else:
			return redirect('/home/')
	else:
		return redirect('/home/')

def logout_view(request):
    if request.user:
        print "logdded out"
        del request.session['type']
        auth.logout(request)
    return redirect('/')
