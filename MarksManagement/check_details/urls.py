from django.urls import path
from . import views

urlpatterns = [
    path('/checkdetails', views.check_details, name='check_details'),
    path('checkdetail/<str:pk>', views.check_detail.as_view(), name='checkdetail'),
]