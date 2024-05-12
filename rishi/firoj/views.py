from django.shortcuts import render,redirect
from django.http import HttpResponse
from firoj.models import *

# Create your views here.

def test(request):
    return HttpResponse('testing the page')

#views for home page
def home(request):
    return render(request,'home.html')
#views for signuppage
def signup(request):
    return render(request,'signup.html')

#views for login
def login(request):
    return render(request,'login.html')

#views for availablecab
def available(request):
    return render(request,'availableC.html')

#views for signup table 
def signupform(request):
    u=customersignupform()
    u.CName=request.GET['name']
    u.CEmail=request.GET['email']
    u.pwd=request.GET['password']
    u.save()
    return render(request,'signup.html')

#views for available cab table
def cab(request):
    u=availablecab()
    u.DName=request.GET['a1']
    u.CNo=request.GET['a2']
    u.DphNo=request.GET['a3']
    u.CType=request.GET['a7']
    u.save()
    return render(request,'availableC.html')

#vews for availblecab table
def showcab(request):
    u=availablecab.objects.all()
    return render(request,'showcab.html',{'a':u})

#vies for logcode
def logcode(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if customersignupform.objects.filter(CEmail=a,pwd=b):
        u=customersignupform.objects.get(CEmail=a,pwd=b)
        return render(request,'booking.html',{'a':u})
    else:
        return render(request,'login.html')
    
def booking(request):
    return render(request,'booking.html')   


def book(request):
    u=customer()
    u.CName=request.GET['a1']
    u.CAddress=request.GET['a2']
    u.CphNo=request.GET['a3']
    u.CEmail=request.GET['a5']
    u.save()
    return render(request,'booking.html')
