from django.shortcuts import render,redirect
from donor.models import *
# Create your views here.


def commingfood(request):
    return render(request,'centre/commingfood.html')


def presentfood(request):
    foods=Food.objects.filter(status='Delivered',is_consumed=False)

    return render(request, 'centre/presentfood.html',{'foods':foods})

def consume(request,pk):
    food=Food.objects.get(pk=pk)
    food.is_consumed=True
    food.save()
    return redirect('centre-presentfood')

def previous(request):
    foods = Food.objects.filter(status='Delivered', is_consumed=True)
    return render(request,'centre/previous.html',{'foods':foods})


