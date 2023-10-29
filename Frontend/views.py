from django.shortcuts import render,redirect, get_object_or_404
from Frontend.models import registrationdb
from Frontend.models import Leave_Request
from Backend.models import registerdb,empdb
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from Backend import views

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def registration(request):
    return render(request,"Registration.html")

def savereg(request):
    if request.method == "POST":
      na = request.POST.get('name')
      em = request.POST.get('email')
      mo = request.POST.get('mobile')
      pw = request.POST.get('password')
      images = request.FILES['images']
      obj = registrationdb(Name=na, Email=em, Mobile=mo, Password=pw, Image=images)
      obj.save()
      messages.success(request,"Registration Succesfull..We will contact you soon")
      return redirect(registration)

def login(request):
  return render(request,"login.html")

def user_reg(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        pa=request.POST.get('password1')
        pa2=request.POST.get('password2')
        obj=registerdb(Name=na,Email=em,Password=pa,C_password=pa2)
        obj.save()
        return redirect(login)



def userlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if registerdb.objects.filter(Name=username_r,Password=password_r).exists():

            request.session['username1'] = username_r
            request.session['password1'] = password_r

            return redirect(profilehome)
        else:
            return redirect(login)
    return redirect(login)

def logout(request):
    del request.session['username1']
    del request.session['password1']
    return redirect(login)

def profilehome(request):
    return render(request,"profile_home.html")

def displayemployee(request):
    empdata=empdb.objects.filter(Name=request.session["username1"])
    return render(request,"Employee_display.html",{"empdata":empdata})

def leave(request):
    leave_requests = Leave_Request.objects.filter(username=request.session["username1"])
    return render(request,"leave.html",{'leave_requests':leave_requests})

def new_leave_request(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        username=request.POST.get('username')
        reason=request.POST.get('reason')
        obj=Leave_Request(date=date,username=username,reason=reason)
        obj.save()

    return redirect(leave)


