from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('company/', views.getCompanys),
    path('addcompany/', views.addCompany),
]

