from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from donor.models import Donor, Food
from .models import Volenteer, Location
from .forms import *
import json
# Create your views here.
from django.core.mail import send_mail

from firstProject import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
# from twilio.rest import Client
#
# account_sid = 'AC83362a0105ba10e6022496ddd9574b12'
# auth_token = '60064eb296c19552875ad031bcfa10c9'
# client = Client(account_sid, auth_token)

import plivo

AUTH_ID = "MANJJLZTG4ZJLJYWVLMD"
AUTH_TOKEN = "ZDc4Y2FjNTZhZmViM2QxOTRjNTg2OTg2NmViYWNk"

client2 = plivo.RestClient(AUTH_ID,AUTH_TOKEN)

def Send(to,body):
    new_mobile = '+92'
    newstr = to[:0] + to[1:]
    new_mobile = new_mobile + newstr
    message_created = client2.messages.create(

        src='+923024506389',

        dst=new_mobile,

        text=body)


# def sendSms(to, body):
#     new_mobile = '+92'
#     newstr = to[:0] + to[1:]
#     new_mobile = new_mobile + newstr
#     message = client.messages.create(
#         from_='+12244772647',  # (224) 477-2647
#         body=body,
#         to=new_mobile
#     )
#
#     return message.sid


@login_required
def change_password(request):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('volunteer-password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def index(request):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    volunteer = Volenteer.objects.get(user=request.user)
    pickups = Food.objects.filter(volunteer=volunteer)
    fast = pickups.filter(food_type='Fast Food').extra({'post_date': "date(post_date)"}).values('post_date').annotate(
        y=Count('id'))
    regular = pickups.filter(food_type='Regular Food').extra({'post_date': "date(post_date)"}).values(
        'post_date').annotate(y=Count('id'))
    fast_food = []
    fast_list = list(fast)
    for d in fast_list:
        data = {
            "x": d["post_date"],
            "y": d["y"]
        }
        fast_food.append(data)
    regular_list = list(regular)
    regular_food = []
    for d in regular_list:
        data = {
            "x": d["post_date"],
            "y": d["y"]
        }
        regular_food.append(data)

    return render(request, 'volunteer/index.html', {'fast': json.dumps(fast_food), 'regular': json.dumps(regular_food)})


def profile(request):
    volunteer = Volenteer.objects.get(user=request.user)
    form = ProfileForm(instance=volunteer)
    pickups = Food.objects.filter(volunteer=volunteer).__len__()
    msg = ""
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=volunteer)
        if form.is_valid():
            volunteer = form.save()
            msg = "Profile Updated Successfully"
            if volunteer.image:
                request.session['pic'] = volunteer.image.url
            else:
                request.session['pic']='/static/images/Student-64.png'
    return render(request, 'volunteer/profile.html', {'form': form, 'msg': msg, 'user1': volunteer, 'pickups': pickups})


def foods(request):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    volunteer = Volenteer.objects.get(user=request.user)
    all_foods = volunteer.food_set.all()

    if request.method == "POST":
        status = request.POST.get('status', "")
        location = request.POST.get('location', "")
        print(request.POST.get('foodId', ''))
        print(location, status)
        foodId = int(request.POST.get('foodId'))
        food = Food.objects.get(pk=foodId)
        food.status = status
        donor=food.donor.first()
        food.delivered_at = location
        food.save()
        body = "\nHello " + donor.user.first_name + " " + donor.user.last_name + "\nThis is to inform you that your  Food: " + food.food_title + " is been devlivered by " + food.volunteer.user.first_name + "\n at "+location+" Please call this number to confirm: " + food.volunteer.mobile
        try:
            # sendSms(donor.mobile,body)
            if status!='Picked':
                send_mail('FDS Notification', body, settings.EMAIL_HOST_USER, [donor.user.email, ])
                Send(donor.mobile, body)
        except:
            print('error in message sending')

    return render(request, 'volunteer/Pickup-list.html', {'foods': all_foods, 'volunteer': volunteer})


def map(request, pk):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    food = Food.objects.get(pk=pk)
    donor = food.donor.first()
    print(donor.map_latitude, donor.map_logitude)
    return render(request, 'volunteer/map.html', {'bLat': donor.map_latitude, 'bLang': donor.map_logitude})


def request(request):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    volunteer = Volenteer.objects.get(user=request.user)
    foods = Food.objects.filter(status='New Entry').exclude(volunteer__isnull=False)

    return render(request, 'volunteer/request.html', {'foods': foods, 'volunteer': volunteer})


def setting(request):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    return render(request, 'volunteer/setting.html')


def accept_food(request, pk):
    if not auth_volunteer(request):
        return redirect('volunteer-profile')
    food = Food.objects.get(pk=pk)
    volunteer = Volenteer.objects.get(user=request.user)
    food.volunteer = volunteer
    food.save()

    donor = food.donor.all()[0]
    print(donor.mobile)
    body = "\nHello " + donor.user.first_name + " " + donor.user.last_name + "\nThis is to inform you that your request for Food: " + food.food_title + " is been accepted by "+food.volunteer.user.first_name+"\n Please call this number to confirm: "+food.volunteer.mobile
    try:
        #sendSms(donor.mobile,body)
        send_mail('FDS Notification', body, settings.EMAIL_HOST_USER, [donor.user.email, ])
        Send(donor.mobile,body)
    except:
        print('error in message sending')
    return redirect('volunteer-request')


def auth_volunteer(request):
    volunteer = Volenteer.objects.filter(user=request.user).first()
    if volunteer:
        if volunteer.is_approved:
            return True
        else:
            return False
    else:
        messages.error(request, 'Please login as donor')
        return False
