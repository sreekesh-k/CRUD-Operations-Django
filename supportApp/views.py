from django.http import HttpResponse
from django.shortcuts import render
from  . models import ItemsInfo
# Create your views here.

def listItems(request):
    return render(request,"list.html")


def edit(request):
    return render(request,"edit.html")


def create(request):
    if request.POST:
       name = request.POST.get("name")
       description = request.POST.get("description")
       quantity = request.POST.get("quantity") 
       newItem = ItemsInfo(name=name,description=description,quantity=quantity)
       newItem.save()
    return render(request,"create.html")