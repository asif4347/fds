from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from fdsadmin.models import Contact
from django.contrib.auth.models import User
from volunteer.models import Volenteer
from donor.models import Donor
from fdsadmin.models import *
# Create your views here.
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            thisUser=User.objects.get(username=username)
            thisUser.email=request.POST.get("email","")
            name = request.POST.get("name", "")
            thisUser.first_name=name
            thisUser.save()
            auth_login(request, user)
            role=request.POST.get("role","")

            if role=="Volunteer":
                volunteer=Volenteer()
                volunteer.name=name
                volunteer.user=thisUser
                volunteer.save()
                return redirect('volunteer-profile')

            if role=="Donor":
                donor=Donor()
                donor.name=name
                donor.user=thisUser
                donor.save()
                return redirect('donor-profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def about(request):
    return render(request, 'home/about.html')

def news(request):
    return render(request, 'home/news.html')


def contact(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name','')
        email=request.POST.get('email','')
        message=request.POST.get('message','')
        cnct=Contact()
        cnct.full_name=full_name
        cnct.email=email
        cnct.message=message
        cnct.save()
    return render(request, 'home/contact.html')


def login(request):
    err=""
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request,user)
            thisUser = User.objects.get(username=username)
            volunteer=Volenteer.objects.filter(user=thisUser).first()
            donor=Donor.objects.filter(user=thisUser).first()
            if volunteer:
                try:
                    request.session['pic']=volunteer.image.url
                except:
                    print("Image Not Found")
                    request.session['pic']="/static/images/Student-64.png"
                return redirect('volunteer-index')
            if donor:
                try:
                    request.session['pic']=donor.image.url
                except:
                    print("Image Not Found")
                    request.session['pic']="/static/images/Student-64.png"
                return redirect('donor-index')
            else:
                fds=FdsAdmin.objects.filter(user=thisUser).first()
                try:
                    request.session['pic']=fds.image.url
                except:
                    print("Image Not Found")
                    request.session['pic']="/static/images/Student-64.png"
                return redirect('fdsadmin-profile')
        else:
            err="username or password is incorrect!"
    return render(request,'login.html',{"err":err})


def logout(request):
    auth_logout(request)
    return redirect('/home/login')


