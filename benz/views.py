from django.shortcuts import render

# Create your views here.

def blue(request):
    return render(request,'blue.html')
