from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery
from student.models import students
from django.views.generic.edit import  UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.
@login_required
def home(request):
    if 'pin' in request.GET:
        pin = request.GET['pin']
        vector = SearchVector('pin_number', 'first_name', 'last_name', 'branch', 'year')
        query =SearchQuery(pin)
        data = students.objects.annotate(search=vector).filter(search=query)
        return render(request,'home.html',{'data':data})
    else:
        return render(request,'home.html')




class student_details(DetailView):
    model = students
    template_name = 'student_details.html'




class update_student_details(UpdateView):
    model = students
    template_name = 'update_student_details.html'
    fields = ['pin_number', 'first_name', 'last_name', 'year', 'branch', 'first_year_101_UT1','first_year_102_UT1',  'first_year_103_UT1' , 'first_year_104_UT1', 'first_year_105_UT1', 'first_year_106_UT1',
    'first_year_101_UT2','first_year_102_UT2','first_year_103_UT2','first_year_104_UT2','first_year_105_UT2','first_year_106_UT2',
    'first_year_107_P','first_year_108_P','first_year_109_P','first_year_110_P',
    'first_year_101_F','first_year_102_F','first_year_103_F','first_year_104_F','first_year_105_F','first_year_106_F','first_year_107_F','first_year_108_F','first_year_109_F','first_year_110_F',
    'second_year_301_UT1','second_year_302_UT1','second_year_303_UT1','second_year_304_UT1','second_year_305_UT1',
    'second_year_301_UT2','second_year_302_UT2','second_year_303_UT2','second_year_304_UT2','second_year_305_UT2',
    'second_year_306_P','second_year_307_P','second_year_308_P','second_year_309_P',
    'second_year_301_F','second_year_302_F','second_year_303_F','second_year_304_F','second_year_305_F','second_year_306_F','second_year_307_F','second_year_308_F','second_year_309_F',
    'second_year_401_UT1','second_year_402_UT1','second_year_403_UT1','second_year_404_UT1','second_year_405_UT1',
    'second_year_401_UT2','second_year_402_UT2','second_year_403_UT2','second_year_404_UT2','second_year_405_UT2',
    'second_year_406_P','second_year_407_P','second_year_408_P','second_year_409_P',
    'second_year_401_F','second_year_402_F','second_year_403_F','second_year_404_F','second_year_405_F','second_year_406_F','second_year_407_F','second_year_408_F','second_year_409_F',
    'third_year_501_UT1','third_year_502_UT1','third_year_503_UT1','third_year_504_UT1','third_year_505_UT1',
    'third_year_501_UT2','third_year_502_UT2','third_year_503_UT2','third_year_504_UT2','third_year_505_UT2',
    'third_year_506_P','third_year_507_P','third_year_508_P','third_year_509_P',
    'third_year_501_F','third_year_502_F','third_year_503_F','third_year_504_F','third_year_505_F','third_year_506_F','third_year_507_F','third_year_508_F','third_year_509_F',
    'third_year_601_F'
    ]

    success_url = '/marks/home'


class delete_student_details(DeleteView):
    model = students
    success_url= '/marks/home'
    template_name = 'delete_student_details.html'


@login_required

def student_home(request):
    if 'pin' in request.GET:
        pin = request.GET['pin']
        vector = SearchVector('pin_number', 'first_name', 'last_name', 'branch', 'year')
        query =SearchQuery(pin)
        data = students.objects.annotate(search=vector).filter(search=query)
        return render(request,'student_home.html',{'data':data})
    else:
        return render(request,'student_home.html')