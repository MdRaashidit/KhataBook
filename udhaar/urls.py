from django.urls import path,include
from.views import *
urlpatterns = [
    path('',home,name='home'),
    path('history/',history,name='history'),
    path('accounts/', include('django.contrib.auth.urls')),
]
