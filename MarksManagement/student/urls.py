from django.urls import path
from . import views

urlpatterns = [
    path('/student', views.student_registration.as_view(), name='student'),
    path('/allstudentdetails', views.all_students.as_view(), name='allstudentstudent')

]