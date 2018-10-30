from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='fdsadmin-index'),
    url(r'^donors$',views.donors,name='fdsadmin-donors'),
    url(r'^volunteers$',views.volunteers,name='fdsadmin-volunteers'),
    url(r'^feedbacks$',views.feedback,name='fdsadmin-feedbacks'),
    url(r'^account-approve$', views.account_approve, name='fdsadmin-account-approve'),
    url(r'^manage-account$', views.manage_account, name='fdsadmin-manage-account'),
    url(r'^profile$', views.profile, name='fdsadmin-profile'),
    url(r'^donor-food$', views.donor_food, name='fdsadmin-donor-food'),
    url(r'^view-volunteers$',views.view_volunteers,name='fdsadmin-view-volunteers'),

]