from django.shortcuts import render,redirect
from Frontend.models import registrationdb
from Backend.models import registerdb,empdb
from Frontend.models import Leave_Request
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
  return render(request,"Index.html")




def displayregister(request):
  registerdata = registrationdb.objects.all()
  return render(request, "displayreg.html", {"registerdata": registerdata})


def editregister(req, dataid):
  editregisterdata = registrationdb.objects.get(id=dataid)
  return render(req, "Edit_reg.html", {"editregisterdata": editregisterdata})


def updateregister(request, dataid):
  if request.method == "POST":
    na = request.POST.get('name')
    em = request.POST.get('email')
    mo = request.POST.get('mobile')
    pw = request.POST.get('password')
    try:
      img = request.FILES.getlist['images']

      fs = FileSystemStorage()
      file = fs.save(img.name, img)
    except MultiValueDictKeyError:
      file = registrationdb.objects.get(id=dataid).Image
    registrationdb.objects.filter(id=dataid).update(Name=na, Email=em, Mobile=mo, Password=pw, Image=file)

    return redirect(displayregister)


def deleteregister(req, dataid):
  deleteregisterdata = registrationdb.objects.filter(id=dataid)
  deleteregisterdata.delete()
  messages.error(req,"Data Deleted")
  return redirect(displayregister)

def dellog(request,dataid):
    deletelogdata = registerdb.objects.filter(id=dataid)
    deletelogdata.delete()
    messages.warning(request, "User Removed")
    return redirect(displayuser)

def send_email_with_link(request):
    recipient_email = 'adithyan2ms@gmail.com'
    subject = 'Your Link to login'

    link = 'http://127.0.0.1:8000/Backend/login'  # Replace with your desired link

    context = {
      'link': link,
    }

    email_body = render_to_string('email_template.html', context)

    send_mail(
      subject,
      '',
      settings.DEFAULT_FROM_EMAIL,
      [recipient_email],
      html_message=email_body
    )
    return redirect(index)

def displayuser(request):
  userregisterdata = registerdb.objects.all()
  return render(request, "display_login.html", {"userregisterdata": userregisterdata})

def employee(request):
    return render(request,"employee_details.html")

def saveemp(request):
    if request.method == "POST":
      na = request.POST.get('name')
      em = request.POST.get('designation')
      mo = request.POST.get('date')

      obj = empdb(Name=na, Designation=em, Date=mo)
      obj.save()
      messages.success(request,"Details added")

      return redirect(employee)

def leaveRequests(request):
   userregisterdata = registerdb.objects.all()
   leave_requests = Leave_Request.objects.all()
   return render(request, "display_leaveRequests.html", {"leave_requests": leave_requests,"userregisterdata": userregisterdata})

def accept_leave_request(request, dataId):
    leave_request = Leave_Request.objects.get(id=dataId)
    leave_request.status = 'Approved'
    leave_request.save()


    return redirect(leaveRequests)


def delete_leave_request(request, dataId):
    leave_request = Leave_Request.objects.get(id=dataId)
    leave_request.delete()
    messages.error(request,"Data Deleted")

    return redirect(leaveRequests)

