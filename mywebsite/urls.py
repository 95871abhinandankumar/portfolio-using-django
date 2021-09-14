from django.urls import path
from . import views
from .views import  projectListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/', projectListView.as_view(), name='projects'),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
] 
