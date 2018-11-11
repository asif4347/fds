from django.contrib.auth.decorators import login_required
from django.db.models import Count
import json
from donor.models import *
from volunteer.models import *
from .models import *
from django.contrib.auth.models import User
from .forms import *
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
            return redirect('fdsadmin-password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'fdsadmin/change_password.html', {
        'form': form
    })

@login_required
def index(request):
    donations = Food.objects.all()
    fast = donations.filter(food_type='Fast Food').extra({'post_date': "date(post_date)"}).values('post_date').annotate(
        y=Count('id'))
    regular = donations.filter(food_type='Regular Food').extra({'post_date': "date(post_date)"}).values(
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
    return render(request, 'fdsadmin/index.html', {'fast':json.dumps(fast_food), 'regular': json.dumps(regular_food)})

@login_required
def donors(request):
    all_donors = Donor.objects.all()
    return render(request, 'fdsadmin/donors.html', {'donors': all_donors})

@login_required
def volunteers(request):
    all_volunteers = Volenteer.objects.all()
    return render(request, 'fdsadmin/volunteers.html', {'volunteers': all_volunteers})

@login_required
def feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'fdsadmin/feedback.html', {'feedbacks': feedbacks})

@login_required
def account_approve(request):
    return render(request, 'fdsadmin/account-approve.html')

@login_required
def manage_account(request):
    return render(request, 'fdsadmin/manage-account.html')

@login_required
def profile(request):
    fdsAdmin = FdsAdmin.objects.filter(user=request.user).first()
    form = ProfileForm(instance=fdsAdmin)
    msg = ""
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=fdsAdmin)
        if form.is_valid():
            fdsAdmin=form.save()
            form = ProfileForm(instance=fdsAdmin)
            msg = "Profile Updated Successfully"
    return render(request, 'fdsadmin/profile.html', {'form': form, 'msg': msg, 'user1': fdsAdmin})

@login_required
def donor_food(request, pk):
    donor = Donor.objects.get(pk=pk)
    all_foods = Food.objects.filter(donor=donor)
    return render(request, 'fdsadmin/donor-food.html', {"foods": all_foods, 'donor': donor})

@login_required
def view_volunteers(request, pk):
    volunteer = Volenteer.objects.get(pk=pk)
    pickups = Food.objects.filter(volunteer=volunteer)
    return render(request, 'fdsadmin/view-volunteers.html', {'pickups': pickups, 'volunteer': volunteer})

@login_required
def donor(request):
    return render(request, 'fdsadmin/donor.html')

@login_required
def volunteer(request):
    return render(request, 'fdsadmin/volunteer.html')

@login_required
def donor_manage(request):
    donors = Donor.objects.all()
    return render(request, 'fdsadmin/donor_manage.html', {'donors': donors})

@login_required
def volunteer_manage(request):
    volunteers = Volenteer.objects.all()
    return render(request, 'fdsadmin/volunteer_manage.html', {'volunteers': volunteers})

@login_required
def block_account(request, username):
    user = User.objects.get(username=username)
    user.is_active = False
    user.save()
    volunteer = Volenteer.objects.filter(user=user).first()
    donor = Donor.objects.filter(user=user).first()
    if volunteer:
        return redirect('fdsadmin-volunteer-manage')

    if donor:
        return redirect('fdsadmin-donor-manage')

@login_required
def unblock_account(request, username):
    user = User.objects.get(username=username)
    user.is_active = True
    user.save()
    volunteer = Volenteer.objects.filter(user=user).first()
    donor = Donor.objects.filter(user=user).first()
    if volunteer:
        return redirect('fdsadmin-volunteer-manage')

    if donor:
        return redirect('fdsadmin-donor-manage')

@login_required
def delete_account(request, username):
    user = User.objects.get(username=username)
    volunteer = Volenteer.objects.filter(user=user).first()
    donor = Donor.objects.filter(user=user).first()
    if volunteer:
        user.delete()
        return redirect('fdsadmin-volunteer-manage')
    if donor:
        user.delete()
        return redirect('fdsadmin-donor-manage')
