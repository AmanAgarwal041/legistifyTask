from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.core import serializers
import json
# Create your views here.
def home(request):
    return render(request,"home.html",{})

def signupuser(request):
	if 'type' in request.session:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/')
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
	if 'type' in request.session:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/')
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
	if 'type' in request.session:
		if request.session['type']=='user':
			return redirect('/userdashboard/')
		elif request.session['type']=='lawyer':
			return redirect('/lawyerdashboard/')
		else:
			return redirect('/')
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
    if 'type' in request.session:
        if request.session['type']=='user':
            try:
                lawyers = serializers.serialize('json', LawyerDetail.objects.all())
                law = json.loads(lawyers)
                lawyer_data = []
                for lawy in law:
                    userInfo = User.objects.get(username=lawy["fields"]["lid"])
                    sendreq = ContactLawyer.objects.filter(uid=request.user,lid=lawy["fields"]["lid"])
                    if sendreq is not None and sendreq:
                        sendStatus = sendreq[0].status
                    else:
                        sendStatus = 0
                    all_detail = {
                            "lid"   : lawy["fields"]["lid"],
                            "speciality"   : lawy["fields"]["speciality"],
                            "age"   : lawy["fields"]["age"],
                            "experience"   : lawy["fields"]["experience"],
                            "pno"   : lawy["fields"]["pno"],
                            "gen"   : lawy["fields"]["gen"],
                            "fname" : userInfo.first_name,
                            "email" : userInfo.email,
                            "status": sendStatus
                    }
                    lawyer_data.append(all_detail)
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
            print len(lawyer_data)
            context = {
                    "lawyer_data":lawyer_data
            }
            return render(request, "UserDashboard.html", context)
        elif request.session['type']=='lawyer':
            return redirect('/lawyerdashboard/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def lawyerdashboard(request):
    if 'type' in request.session:
        if request.session['type']=='lawyer':
            try:
                users_data = serializers.serialize('json', ContactLawyer.objects.filter(lid=request.user))
                users_dt = json.loads(users_data)
                users_dt_total = []
                print "Test",users_dt
                for usdt in users_dt:
                    userInfo = User.objects.get(username=usdt["fields"]["uid"])
                    userInfo_total = UserDetail.objects.get(uid=usdt["fields"]["uid"])
                    all_detail = {
                            "uid"   : usdt["fields"]["uid"],
                            "age"   : userInfo_total.age,
                            "pno"   : userInfo_total.pno,
                            "gen"   : userInfo_total.gen,
                            "fname" : userInfo.first_name,
                            "email" : userInfo.email,
                            "status": usdt["fields"]["status"],
                            "contact_id":usdt["pk"]
                        }
                    users_dt_total.append(all_detail)
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
            print len(users_dt_total)
            context = {
                    "user_data":users_dt_total
            }
            return render(request, "LawyerDashboard.html", context)
        elif request.session['type']=='user':
			return redirect('/userdashboard/')
        else:
			return redirect('/')
    else:
		return redirect('/')

def logout_view(request):
    if request.user:
        print "logdded out"
        del request.session['type']
        auth.logout(request)
    return redirect('/')

def send_request(request):
    if 'type' in request.session:
        if request.session['type']=='user':
            try:
                lid = request.GET['lid']
                print "Test :",lid
                ContactLawyer.objects.create(uid=request.user, lid=lid, status=2).save()
            except Exception as e:
				print '%s (%s)' % (e.message, type(e))
            return redirect('/userdashboard/')
        elif request.session['type']=='lawyer':
            return redirect('/lawyerdashboard/')
        else:
			return redirect('/')
    else:
		return redirect('/')

def accept_request(request):
    if 'type' in request.session:
        if request.session['type']=='user':
            return redirect('/userdashboard/')
        elif request.session['type']=='lawyer':
            try:
                contact_id = request.GET['contact_id']
                ContactLawyer.objects.filter(pk=contact_id).update(status=1).save()
            except Exception as e:
				print '%s (%s)' % (e.message, type(e))
            return redirect('/lawyerdashboard/')
        else:
            return redirect('/')
    else:
        return redirect('/')
def reject_request(request):
    if 'type' in request.session:
        if request.session['type']=='user':
            return redirect('/userdashboard/')
        elif request.session['type']=='lawyer':
            try:
                contact_id = request.GET['contact_id']
                ContactLawyer.objects.filter(pk=contact_id).update(status=3).save()
            except Exception as e:
				print '%s (%s)' % (e.message, type(e))
            return redirect('/lawyerdashboard/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def pending_request(request):
    if 'type' in request.session:
        if request.session['type']=='user':
            return redirect('/userdashboard/')
        elif request.session['type']=='lawyer':
            try:
                contact_id = request.GET['contact_id']
                ContactLawyer.objects.filter(pk=contact_id).update(status=2).save()
            except Exception as e:
				print '%s (%s)' % (e.message, type(e))
            return redirect('/lawyerdashboard/')
        else:
			return redirect('/')
