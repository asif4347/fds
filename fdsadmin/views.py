from django.shortcuts import render

# Create your views here.

def index(request):
    return  render(request,'fdsadmin/index.html')

def donors(request):
    return  render(request,'fdsadmin/donors.html')


def volunteers(request):
    return  render(request,'fdsadmin/volunteers.html')


def feedback(request):
    return  render(request,'fdsadmin/feedback.html')


def account_approve(request):
    return  render(request, 'fdsadmin/account-approve.html')

def manage_account(request):
    return  render(request,'fdsadmin/manage-account.html')

def profile(request):
    return  render(request,'fdsadmin/profile.html')

def donor_food(request):
    return  render(request,'fdsadmin/donor-food.html')

def view_volunteers(request):
    return  render(request,'fdsadmin/view-volunteers.html')

