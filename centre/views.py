from django.shortcuts import render

# Create your views here.


def commingfood(request):
    return render(request,'centre/commingfood.html')


def presentfood(request):
    return render(request, 'centre/presentfood.html')


def previous(request):
    return render(request,'centre/previous.html')


