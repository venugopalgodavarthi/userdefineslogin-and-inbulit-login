
from django.shortcuts import render,reverse
from userlogin import forms 
from userlogin import models 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def base(request):
    return render(request,"userbase.html")

def Register(request):
    form = forms.Reg()
    if request.method=="POST":
        form=forms.Reg(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"registration successfull.") #sending the msg in sample page and displaying message
            return HttpResponseRedirect('/login/?success=1') #sending the msg to differnt page and displaying message
    form = forms.Reg()
    return render(request,"userregister.html",{'form':form,"message":messages})


def Login(request):
    form = forms.Login()
    if request.method=="POST":
        form=forms.Login(request.POST)
        if form.is_valid():
            p1=models.login.objects.filter(email= form.cleaned_data['usermail'], password=form.cleaned_data['password'],)
            usermail= form.cleaned_data['usermail']
            password=form.cleaned_data['password'] 
            print(usermail)
            print(password)
            u=0
            p=0
            for i in p1:
                u=i.email
                p=i.password
            if usermail==u and password==p:
                return render(request,"userhome.html",{'form':p1})
            else:
                messages.error(request,"usermail and password is wrong either user not register")
                return HttpResponseRedirect('/login/?error=1')
    return render(request,"userlogin.html",{'form':form})

def Home(request):
    return render(request,"userhome.html")
    


