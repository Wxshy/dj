from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return render(request, 'homepage/homepage.html')

def about(request):
    return render(request, 'homepage/about.html')