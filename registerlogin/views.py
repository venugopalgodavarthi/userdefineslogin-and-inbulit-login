from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from registerlogin.forms import NewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register_req(request):
    if request.method=='POST':
        print("haii")
        form= NewUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data["username"])
            user = form.save()
            login(request, user)
            messages.success(request,"registration successfully.")
        else:
            messages.error(request,"unsuccessfully registration ")
    form = NewUser()
    return render(request,"register.html",{"register_form":form})

def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username,password)
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"login by mr {username}loggd in.")
                return HttpResponseRedirect(reverse('home'))
                #return redirect('home')
            else:
                messages.error(request,"invalid username and password")
        else:
            messages.error(request,"invalid username and password")
    form= AuthenticationForm
    return render(request,"login.html",{"login_form":form})

def home_req(request):
    return render(request,"home.html")

def logout_req(request):
    logout(request)
    messages.info(request,"you have successfully logged out")
    return redirect('home')
    