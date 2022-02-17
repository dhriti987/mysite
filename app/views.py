from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    query = Person.objects.all()
    return render(request,'home.html',{'data':query})

def home(request):
    data = request.GET.get('name')
    return render(request,'payal.html',{'data':data})

def result(request):
    x = int(request.POST['num1'])
    y = int(request.POST['num2'])
    res = x+y
    return render(request,'result.html',{'result':res})