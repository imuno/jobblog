from django.shortcuts import render

from .models import Job

jobs = Job.objects
# Create your views here.

def home(request):
    return render(request, 'jobs/home.html', {'jobs':jobs})
