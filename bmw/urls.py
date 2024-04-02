from django.urls import path
from bmw.views import *
app_name='anything'

urlpatterns = [
    path('black/',black,name='black'),
]