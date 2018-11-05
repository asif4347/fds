from django.shortcuts import render,redirect
from .forms import FeedbackForm,FoodForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Donor,Food
# Create your views here.

@login_required
def index(request):
    return  render(request,'donor/index.html')

@login_required
def profile(request):
    donor = Donor.objects.get(user=request.user)
    msg=""
    form=ProfileForm(instance=donor)
    if request.method=="POST":
        form=ProfileForm(request.POST,instance=donor)
        if form.is_valid():
            form.save()
            msg="Profile Updated Successfully"
    return  render(request,'donor/profile.html',{'form':form,'msg':msg})

@login_required
def foods(request):
    donor = Donor.objects.get(user=request.user)
    food_list=Food.objects.filter(donor=donor)
    if request.method=="POST":
        form=FoodForm(request.POST)
        if form.is_valid():
            food=Food()

            food.food_title=form.cleaned_data.get('food_title')
            food.food_type=form.cleaned_data.get('food_type')
            food.preparation_date=form.cleaned_data.get('preparation_date')
            food.post_date=form.cleaned_data.get('post_date')
            food.quantity=form.cleaned_data.get('quantity')
            food.save()
            food.donor.add(donor)
            food.save()
    else:
        form=FoodForm(initial={'donor':donor})
    return render(request,'donor/foods-list.html',{"form":form,'food_list':food_list})

@login_required
def map(request):
    return  render(request,'donor/map.html')
@login_required
def setting(request):
    return  render(request,'donor/setting.html')
@login_required
def rating(request):
    return  render(request,'donor/rating.html')

@login_required
def feedback(request):
    msg=""
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            msg="feedback submitted successfully"
            form = FeedbackForm()
    else:
        form=FeedbackForm()
    return render(request,'donor/feedback.html',{"form":form,'msg':msg})

def term_policy(request):
    return  render(request,'donor/term-policy.html')