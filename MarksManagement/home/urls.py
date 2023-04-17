from django.urls import path
from . import views

urlpatterns = [
    path('/home', views.home, name='home'),
    path('/studentdetails/<str:pk>',views.student_details.as_view(), name='studentdetails'),
    path('/updatestudentdetails/<str:pk>',views.update_student_details.as_view(), name='updatestudentdetails'),
    path('/deletestudentdetails/<str:pk>',views.delete_student_details.as_view(), name='deletestudentdetails'),


]