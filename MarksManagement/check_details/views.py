from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchQuery
from student.models import students
from django.views.generic.detail import DetailView

# Create your views here.
def check_details(request):
    if 'pin' in request.GET:
        pin = request.GET.get('pin')
        vector = SearchVector('pin_number', 'first_name', 'last_name', 'branch', 'year')
        query =SearchQuery(pin)
        data = students.objects.annotate(search=vector).filter(search=query)
        return render(request,'check_details.html',{'data':data})
    else:
        return render(request,'check_details.html')



class check_detail(DetailView):
    model = students
    template_name = 'check_detail.html'