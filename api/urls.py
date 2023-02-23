from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.getData),
    path('company/', views.getCompanys),
    path('addcompany/', views.addCompany),
]

router = routers.SimpleRouter()
router.register(r'member', views.MemberViewSet)

urlpatterns += [
    path('', include(router.urls)),
]


