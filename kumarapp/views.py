from django.shortcuts import render
from django.http import HttpResponse
from.models import Login
def home(request):
    post=Login.objects.all()
    return render(request, "first.html",{'post':post})
def rem(request):
    return render(request,"second.html")