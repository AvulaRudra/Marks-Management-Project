from turtle import st
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import studentsform
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from .models import students
from django.db.models import F
from django.contrib.auth.decorators import login_required


# Create your views here.



class student_registration(CreateView):
    model = students
    template_name = 'student_registration.html'
    fields = ['pin_number', 'first_name', 'last_name','branch' ,'year']
    success_url = 'home'
     


class all_students(ListView):
    model = students
    template_name = 'all_student_details.html'
