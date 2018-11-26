from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='donor-index'),
    url(r'^profile$',views.profile,name='donor-profile'),
    url(r'^foods$',views.foods,name='donor-foods'),
    url(r'^map$',views.map,name='donor-map'),
    url(r'^setting$', views.setting, name='donor-setting'),
    url(r'^rating$', views.rating, name='donor-rating'),
    url(r'^feedback$', views.feedback, name='donor-feedback'),
    url(r'^term policy$', views.term_policy, name='donor-term-policy'),
    url(r'food/(?P<pk>\d+)/delete',views.delete,name='delete-food'),
    url(r'food/(?P<pk>\d+)/updated',views.update,name='update-food'),
    url(r'^password/$', views.change_password, name='change_password'),
]
