from django.urls import path
from benz.views import *
app_name='anything'

urlpatterns = [
    path('blue/',blue,name='blue'),
]