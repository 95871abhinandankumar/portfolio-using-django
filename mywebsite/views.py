from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Projects
# Create your views here.


def projects(request):
    context = {
        'projects': Projects.objects.all()
    }
    return render(request, 'projects.html', context)



class projectListView(ListView):
    model = Projects
    template_name = 'projects.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']




def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
