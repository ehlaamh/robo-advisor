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

def loginpage(request):
    if request.method=='POST':
        try:
            Userdetails= Userreg.objects.get(email= request.POST['email'], password = request.POST['password'])
            request.session['email']= Userdetails.email
            return render(request,'robo.html')
        except Userreg.DoesNotExist as e:
            messages.success(request,'Email or Password is invalid..!')
    return render(request,'login.html')
