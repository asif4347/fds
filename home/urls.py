
from django.urls import path
from . import  views
from django.conf.urls import url

urlpatterns = [
 url(r'^$',views.index,name='index'),
 path('index/',views.index),
 path('about/',views.about),
 path('news/', views.news),
 path('register/',views.register),
 path('contact/', views.contact),
 path('login/', views.login),
 path('logout/', views.logout),

]
