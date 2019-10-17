from django.urls import path
from . import views


app_name = 'gmap'

urlpatterns = [
    path('', views.index, name='index'),
    ]