from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.index, name='index'),

    # ex: /company/5/
    path('<int:company_id>/', views.detail, name='detail'),
]