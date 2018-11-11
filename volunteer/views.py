from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render,redirect
from donor.models import Donor, Food
from .models import Volenteer,Location
from .forms import *
import json
# Create your views here.

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


@login_required
def change_password(request):
    if not auth_volunteer(request):
        return redirect('/home/login')
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
        return redirect('/home/login')
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

    return render(request, 'volunteer/index.html',{'fast':json.dumps(fast_food), 'regular': json.dumps(regular_food)})


def profile(request):
    volunteer = Volenteer.objects.get(user=request.user)
    form=ProfileForm(instance=volunteer)
    pickups=Food.objects.filter(volunteer=volunteer).__len__()
    msg = ""
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=volunteer)
        if form.is_valid():
            volunteer = form.save()
            msg = "Profile Updated Successfully"
            request.session['pic'] = volunteer.image.url
    return render(request, 'volunteer/profile.html',{'form':form,'msg':msg,'user1':volunteer,'pickups':pickups})


def foods(request):
    if not auth_volunteer(request):
        return redirect('/home/login')
    volunteer = Volenteer.objects.get(user=request.user)
    all_foods=volunteer.food_set.all()

    if request.method=="POST":
        status=request.POST.get('status',"")
        location=request.POST.get('location',"")
        food=Food.objects.get(pk=request.POST.get('foodId',''))
        food.status=status
        food.delivered_at=location
        food.save()
    return render(request, 'volunteer/Pickup-list.html',{'foods':all_foods,'volunteer':volunteer})


def map(request):
    if not auth_volunteer(request):
        return redirect('/home/login')
    return render(request, 'volunteer/map.html')


def request(request):
    if not auth_volunteer(request):
        return redirect('/home/login')
    volunteer=Volenteer.objects.get(user=request.user)
    foods=Food.objects.filter(status='New Entry').exclude(volunteer__isnull=False)

    return render(request, 'volunteer/request.html',{'foods':foods,'volunteer':volunteer})


def setting(request):
    if not auth_volunteer(request):
        return redirect('/home/login')
    return render(request, 'volunteer/setting.html')


def accept_food(request,pk):
    if not auth_volunteer(request):
        return redirect('/home/login')
    food=Food.objects.get(pk=pk)
    volunteer = Volenteer.objects.get(user=request.user)
    food.volunteer=volunteer
    food.save()
    return redirect('volunteer-request')



def auth_volunteer(request):
    volunteer=Volenteer.objects.filter(user=request.user).first()
    if volunteer:
        if volunteer.is_approved:
            return True
        else:
            return False
    else:
        messages.error(request, 'Please login as donor')
        return False
