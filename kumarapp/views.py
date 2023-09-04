from django.shortcuts import render
from django.http import HttpResponse
from.models import Login
def home(request):
    
    return render(request, "first.html")
