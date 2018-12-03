from  django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='volunteer-index'),
    url(r'^profile$',views.profile,name='volunteer-profile'),
    url(r'^foods$',views.foods,name='volunteer-pickups'),
    url(r'^map/(?P<pk>\d+)$',views.map,name='volunteer-map'),
    url(r'^request$', views.request, name='volunteer-request'),
    url(r'^setting$', views.setting, name='volunteer-setting'),
    url(r'food/(?P<pk>\d+)/accept', views.accept_food, name='accept-food'),
    url(r'^password/$', views.change_password, name='volunteer-password'),

]