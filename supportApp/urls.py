from django.urls import path
from . import views

urlpatterns = [
    path('', views.listItems,name="list"),
    path('create/', views.create,name="create"),
    path('edit/', views.edit,name="edit"),
]
