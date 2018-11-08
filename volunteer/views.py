from django.shortcuts import render,redirect
from donor.models import Donor, Food
from .models import Volenteer,Location
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'volunteer/index.html')


def profile(request):
    return render(request, 'volunteer/profile.html')


def foods(request):
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
    return render(request, 'volunteer/map.html')


def request(request):
    volunteer=Volenteer.objects.get(user=request.user)
    foods=Food.objects.filter(status='New Entry').exclude(volunteer__isnull=False)

    return render(request, 'volunteer/request.html',{'foods':foods,'volunteer':volunteer})


def setting(request):
    return render(request, 'volunteer/setting.html')


def accept_food(request,pk):
    food=Food.objects.get(pk=pk)
    volunteer = Volenteer.objects.get(user=request.user)
    food.volunteer=volunteer
    food.save()
    return redirect('volunteer-request')