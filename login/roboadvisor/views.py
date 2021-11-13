from django.http.response import HttpResponse
from django.shortcuts import render
from roboadvisor.models import Userreg
from django.contrib import messages
from django.shortcuts import redirect

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
            return redirect("http://192.168.0.104:8501")
        except Userreg.DoesNotExist as e:
            messages.success(request,'Email or Password is invalid..!')
    return render(request,'login.html')

def homepage(request):
    return render(request,'home.html')

def mpage(request):
    return redirect("http://stackoverflow.com/")

def predict(request):
    if request.method == 'POST':
        temp={}
        temp['age']=request.POST.get('age')
        temp['rt']=request.POST.get('rt')
        temp['ny']=request.POST.get('ny')
        temp['ai']=request.POST.get('ai')
        
    context={'a':''}
    return render(request, 'mpage.html', context)
    

   