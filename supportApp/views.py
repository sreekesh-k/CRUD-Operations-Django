from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def listItems(request):
    return render(request,"list.html")


def edit(request):
    return render(request,"edit.html")


def create(request):
    return render(request,"create.html")