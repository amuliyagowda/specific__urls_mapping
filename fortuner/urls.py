from django.urls import path
from fortuner.views import *
app_name='something'

urlpatterns = [
    path('white/',white,name='white'),
]
