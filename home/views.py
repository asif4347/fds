from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from fdsadmin.models import Contact
from django.contrib.auth.models import User

from firstProject import settings
from volunteer.models import Volenteer
from donor.models import Donor
from fdsadmin.models import *
# Create your views here.
from django.contrib.auth import logout as auth_logout
from volunteer.views import send_mail

from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def index(request):
    return render(request, 'home/index.html')

def checkpoint(request):
    msg=''
    if request.method=='POST':
        thisUser=request.user
        volunteer = Volenteer.objects.filter(user=thisUser).first()
        donor = Donor.objects.filter(user=thisUser).first()
        code = request.POST.get('code', '')
        if volunteer:

            if volunteer.code == int(code):
                volunteer.code=0
                volunteer.save()
                try:
                    request.session['pic'] = volunteer.image.url
                except:
                    print("Image Not Found")
                    request.session['pic'] = "/static/images/Student-64.png"
                return redirect('volunteer-index')
            else:
                msg="Wrong code!"

        if donor:

            if donor.code == int(code):
                donor.code = 0
                donor.save()
                try:
                    request.session['pic'] = donor.image.url
                except:
                    print("Image Not Found")
                    request.session['pic'] = "/static/images/Student-64.png"
                return redirect('donor-index-index')
            else:
                msg = "Wrong code!"
    return render(request, 'home/checkpoint.html',{'msg':msg})


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
            code =random_with_N_digits(4)
            body="Please enter the digit  "+str(code)+"  to verify you account."
            send_mail('FDS code verification', body, settings.EMAIL_HOST_USER, [thisUser.email, ])
            if role=="Volunteer":
                volunteer=Volenteer()
                volunteer.name=name
                volunteer.user=thisUser
                volunteer.code=code
                volunteer.save()
                if volunteer.code !=0:
                    return redirect('/checkpoint')
                return redirect('volunteer-profile')

            if role=="Donor":
                donor=Donor()
                donor.name=name
                donor.user=thisUser
                donor.code=code
                donor.save()
                if donor.code !=0:
                    return redirect('/checkpoint')
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
                if volunteer.code !=0:
                    return redirect('/checkpoint')
                try:
                    request.session['pic']=volunteer.image.url
                except:
                    print("Image Not Found")
                    request.session['pic']="/static/images/Student-64.png"
                return redirect('volunteer-index')
            if donor:
                if volunteer.code !=0:
                    return redirect('/checkpoint')
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


