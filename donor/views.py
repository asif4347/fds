from django.db.models import Count
from django.shortcuts import render, redirect
from .forms import FeedbackForm, FoodForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import *
from fdsadmin.models import Rating

# Create your views here.

@login_required
def index(request):
    donor = Donor.objects.get(user=request.user)
    donations = Food.objects.filter(donor=donor)
    fast = donations.filter(food_type='Fast Food').extra({'post_date': "date(post_date)"}).values('post_date').annotate(
        count=Count('id'))
    regular = donations.filter(food_type='Regular Food').extra({'post_date': "date(post_date)"}).values(
        'post_date').annotate(count=Count('id'))
    return render(request, 'donor/index.html', {'fast': fast, 'regular': regular})


@login_required
def profile(request):
    donor = Donor.objects.get(user=request.user)
    donations = Food.objects.filter(donor=donor).__len__()
    msg = ""
    form = ProfileForm(instance=donor)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES, instance=donor)
        if form.is_valid():
            form.save()
            msg = "Profile Updated Successfully"
    return render(request, 'donor/profile.html', {'form': form, 'msg': msg, 'donations': donations, 'user': donor})


@login_required
def foods(request):
    donor = Donor.objects.get(user=request.user)
    food_list = Food.objects.filter(donor=donor)
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = Food()
            food.food_title = form.cleaned_data.get('food_title')
            food.food_type = form.cleaned_data.get('food_type')
            food.preparation_date = form.cleaned_data.get('preparation_date')
            food.post_date = form.cleaned_data.get('post_date')
            food.quantity = form.cleaned_data.get('quantity')
            food.save()
            food.donor.add(donor)
            food.save()
    else:
        form = FoodForm(initial={'donor': donor})
    return render(request, 'donor/foods-list.html', {"form": form, 'food_list': food_list})


@login_required
def map(request):
    return render(request, 'donor/map.html')


@login_required
def setting(request):
    return render(request, 'donor/setting.html')


@login_required
def rating(request):
    msg=""
    if request.method=="POST":
        rate=request.POST.get('rate',"")
        rating=Rating()
        rating.rate=rate
        rating.user=request.user
        rating.save()
        msg="Thank you for rating us!"
    return render(request, 'donor/rating.html',{'msg':msg})


@login_required
def feedback(request):
    msg = ""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "feedback submitted successfully"
            form = FeedbackForm()
    else:
        form = FeedbackForm()
    return render(request, 'donor/feedback.html', {"form": form, 'msg': msg})


@login_required
def delete(request, pk):
    food = Food.objects.get(pk=pk)
    food.delete()
    return redirect('donor-foods')


@login_required
def update(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('donor-foods')
    else:
        form = FoodForm(instance=food)
    return render(request, 'donor/update.html', {'form': form})


def term_policy(request):
    return render(request, 'donor/term-policy.html')
