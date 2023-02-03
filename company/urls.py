from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.home, name='home'),

    # ex: /company
    path('company/', views.company, name='company'),

    # ex: /company/5/
    path('company/<int:company_id>/', views.detail, name='detail'),
]