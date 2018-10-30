from django.shortcuts import render

# Create your views here.


def index(request):
    return  render(request,'volunteer/index.html')


def profile(request):
    return  render(request,'volunteer/profile.html')


def foods(request):
    return  render(request,'volunteer/Pickup-list.html')


def map(request):
    return  render(request,'volunteer/map.html')
def request(request):
    return  render(request,'volunteer/request.html')
def setting(request):
    return  render(request,'volunteer/setting.html')