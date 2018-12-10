from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^commingfood$',views.commingfood,name='centre-commingfood'),
    url(r'^presentfood$',views.presentfood,name='centre-presentfood'),
    url(r'^previous$',views.previous,name='centre-previous'),
    url(r'^consume/(?P<pk>\d+)$',views.consume,name='centre-consume'),


]
