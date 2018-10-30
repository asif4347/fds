from django.shortcuts import render

# Create your views here.


def index(request):
    return  render(request,'donor/index.html')


def profile(request):
    return  render(request,'donor/profile.html')


def foods(request):
    return  render(request,'donor/foods-list.html')


def map(request):
    return  render(request,'donor/map.html')

def setting(request):
    return  render(request,'donor/setting.html')

def rating(request):
    return  render(request,'donor/rating.html')

def feedback(request):
    return  render(request,'donor/feedback.html')
def term_policy(request):
    return  render(request,'donor/term-policy.html')