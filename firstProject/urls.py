
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include


from home import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    url(r'^',include('home.urls')),
    url(r'donor/',include('donor.urls')),
    url(r'volunteer/',include('volunteer.urls')),
    url(r'fdsadmin/',include('fdsadmin.urls')),

]
