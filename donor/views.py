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
from django.core.mail import send_mail

from firstProject import settings

@login_required
def change_password(request):
    if not auth_donor(request):
        return redirect('donor-profile')

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
    if not auth_donor(request):
        return redirect('donor-profile')

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
    # if not auth_donor(request):
    #     return redirect('donor-profile')
    donor = Donor.objects.get(user=request.user)
    donations = Food.objects.filter(donor=donor).__len__()
    msg = ""
    form = ProfileForm(instance=donor)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=donor)
        if form.is_valid():
            donor=form.save()
            msg = "Profile Updated Successfully"
            if donor.image:
                request.session['pic'] = donor.image.url
            else:
                request.session['pic']='/static/images/Student-64.png'
            send_mail('FDS Notification',"Your profile updated successfully",settings.EMAIL_HOST_USER,[donor.user.email,])
    return render(request, 'donor/profile.html', {'form': form, 'msg': msg, 'donations': donations, 'user1': donor})


@login_required
def foods(request):
    if not auth_donor(request):
        return redirect('donor-profile')
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
            for file in request.FILES.getlist('gallery'):
                foodImg=FoodImage()
                foodImg.image=file
                foodImg.save()
                food.gallery.add(foodImg)
            food.save()
    else:
        form = FoodForm(initial={'donor': donor})
    return render(request, 'donor/foods-list.html', {"form": form, 'food_list': food_list})


@login_required
def map(request):
    if not auth_donor(request):
        return redirect('donor-profile')
    if request.method=="POST":
        donor = Donor.objects.get(user=request.user)
        donor.map_latitude=request.POST.get('lat','')
        donor.map_logitude=request.POST.get('lang','')
        donor.save()
    return render(request, 'donor/map.html')


@login_required
def setting(request):
    if not auth_donor(request):
        return redirect('donor-profile')
    return render(request, 'donor/setting.html')


@login_required
def rating(request):
    if not auth_donor(request):
        return redirect('donor-profile')
    msg = ""
    if request.method == "POST":
        rate = request.POST.get('rating', "")
        print(rate)
        rating = Rating()
        rating.rate = rate
        rating.user = request.user
        rating.save()
        msg = "Thank you for rating us!"
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

    return render(request, 'donor/rating.html',
                  {'msg': msg, 'user_rating': user_rating, 'avg': sumRating / total, 'total': total, 'rates': rates,
                   'percents': percents})


@login_required
def feedback(request):
    if not auth_donor(request):
        return redirect('donor-profile')
    msg = ""
    feedbacks=Feedback.objects.filter(user=request.user)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed=form.save()
            feed.user=request.user
            feed.save()
            msg = "feedback submitted successfully"
            form = FeedbackForm()
    else:
        form = FeedbackForm()
    return render(request, 'donor/feedback.html', {"form": form, 'msg': msg,'feedbacks':feedbacks})


@login_required
def delete(request, pk):
    if not auth_donor(request):
        return redirect('donor-profile')
    food = Food.objects.get(pk=pk)
    food.delete()
    return redirect('donor-foods')


@login_required
def update(request, pk):
    if not auth_donor(request):
        return redirect('donor-profile')
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

def gallery(request,pk):
    food=Food.objects.get(pk=pk)
    links=[]
    for image in food.gallery.all():
        links.append(image.image)
        links.append(image.image)
    return render(request,'gallery.html',{'images':food.gallery.all()})

def auth_donor(request):
    donor=Donor.objects.filter(user=request.user).first()
    if donor:
        if donor.is_approved:
            return True
        else:
            return False
    else:
        messages.error(request, 'Please login as donor')
        return False
