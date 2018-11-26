from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='fdsadmin-index'),
    url(r'^donors$',views.donors,name='fdsadmin-donors'),
    url(r'^volunteers$',views.volunteers,name='fdsadmin-volunteers'),
    url(r'^feedbacks$',views.feedback,name='fdsadmin-feedbacks'),
    url(r'^account-approve/(?P<username>\w+)$', views.account_approve, name='fdsadmin-account-approve'),
    url(r'^manage-account$', views.manage_account, name='fdsadmin-manage-account'),
    url(r'^profile$', views.profile, name='fdsadmin-profile'),
    url(r'^donor-food/(?P<pk>\d+)', views.donor_food, name='fdsadmin-donor-food'),
    url(r'^view-volunteers/(?P<pk>\d+)$',views.view_volunteers,name='fdsadmin-view-volunteers'),
    url(r'^donor$', views.donor, name='fdsadmin-donor'),
    url(r'^volunteer$',views.volunteer,name='fdsadmin-volunteer'),
    url(r'^donor-manage$', views.donor_manage, name='fdsadmin-donor-manage'),
    url(r'^volunteer-manage$',views.volunteer_manage,name='fdsadmin-volunteer-manage'),
    url(r'^block-user/(?P<username>\w+)',views.block_account,name="block-account"),
    url(r'^unblock-user/(?P<username>\w+)',views.unblock_account,name="unblock-account"),
    url(r'^delete-user/(?P<username>\w+)',views.delete_account,name="delete-account"),
    url(r'^password/$', views.change_password, name='fdsadmin-password'),
]