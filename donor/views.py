from math import floor, ceil, fsum
from django.db.models import Count
from django.shortcuts import render, redirect
from .forms import FeedbackForm, FoodForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import *
from fdsadmin.models import Rating
import json
# Create your views here.

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'donor/change_password.html', {
        'form': form
    })


@login_required
def index(request):
    donor = Donor.objects.get(user=request.user)
    donations = Food.objects.filter(donor=donor)
    fast = donations.filter(food_type='Fast Food').extra({'post_date': "date(post_date)"}).values('post_date').annotate(
        y=Count('id'))
    regular = donations.filter(food_type='Regular Food').extra({'post_date': "date(post_date)"}).values(
        'post_date').annotate(y=Count('id'))
    fast_food=[]
    fast_list=list(fast)
    for d in fast_list:
        data = {
            "x": d["post_date"],
            "y": d["y"]
        }
        fast_food.append(data)
    regular_list=list(regular)
    regular_food=[]
    for d in regular_list:
        data={
            "x":d["post_date"],
            "y":d["y"]
        }
        regular_food.append(data)
    print(regular_food,fast_food)
    return render(request, 'donor/index.html', {'fast':json.dumps(fast_food), 'regular': json.dumps(regular_food)})


@login_required
def profile(request):
    donor = Donor.objects.get(user=request.user)
    donations = Food.objects.filter(donor=donor).__len__()
    msg = ""
    form = ProfileForm(instance=donor)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=donor)
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
        image = request.FILES.get('image')
        print(image)
        if form.is_valid():
            food=form.save()
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
    msg = ""
    user_rating = Rating.objects.filter(user=request.user)
    all_ratings = Rating.objects.all()
    total = all_ratings.__len__()
    rates = [0, 0, 0, 0, 0]
    sumRating = 0
    for r in all_ratings:
        sumRating = sumRating + r.rate
        rates[r.rate - 1] += 1
    percents = [0, 0, 0, 0, 0]
    i = 0
    for n in rates:
        percents[i] = ceil((n / total) * 100)
        i += 1

    print(rates, sumRating / total, percents)
    if request.method == "POST":
        rate = request.POST.get('rating', "")
        rating = Rating()
        rating.rate = rate
        rating.user = request.user
        rating.save()
        msg = "Thank you for rating us!"
    return render(request, 'donor/rating.html',
                  {'msg': msg, 'user_rating': user_rating, 'avg': sumRating / total, 'total': total, 'rates': rates,
                   'percents': percents})


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
