from django.shortcuts import render
from roboadvisor.models import Userreg
from django.contrib import messages

def Userregistration(request):
    if request.method=='POST':
       if request.POST.get('name') and  request.POST.get('email') and request.POST.get('password'):
           saverecord = Userreg()
           saverecord.name=request.POST.get('name')
           saverecord.email=request.POST.get('email')
           saverecord.password=request.POST.get('password')
           saverecord.save()
           messages.success(request,"New user registered successfuly!!")
           return render(request, 'register.html')
    else:
         return render(request, 'register.html')
