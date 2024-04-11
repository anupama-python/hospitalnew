from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from hospitalapp.models import Departments, Doctors


# Create your views here.
def base(request):
    return render(request,'base.html')

def contact(request):
    return render(request,'contact.html')

def departments(request):
    dict_dept={
        'dep':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)

def doctors(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def aboutus(request):
    return render(request,'aboutus.html')

def booking(request):
    if request.method=='POST':
        Patient_Name=request.POST.get("Patient_Name")
        Patient_Phone=request.POST.get("Patient_Phone")
        user=auth.authenticate(Patient_Name=Patient_Name,Patient_Phone=Patient_Phone)
        if user is not None:
            auth.login(request,user)
            return render(request,"message.html")
        else:
            messages.info(request,"invalid")
            return render(request,"message.html")
    return render(request,"booking.html")


    return render(request,'booking.html')

def message(request):
    return render(request,'message.html')
def history(request):
    return render(request,"aboutus.html")
