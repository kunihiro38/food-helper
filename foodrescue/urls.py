from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ContactFormView, ContactResultView #0915Dnagoでお問い合わせフォームを作成する

app_name = "foodrescue"

# 基本構成pathの第一引数が、URLの表示になる
urlpatterns = [

    path("", views.index, name="index"),
    path('index', views.index, name='index'),
    path('loginscreen', views.loginscreen, name='loginscreen'),
    path('operation', views.operation, name='operation'),
    path("service", views.service, name='service'),
    path('privacy', views.privacy, name='privacy'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
    path('required', views.required, name='required'),
    path('mainvisual', views.mainvisual, name='mainvisual'),
    path('search', views.search, name='search'),
    path('imagelist', views.imagelist, name='imagelist'),
    path('zoomimage', views.zoomimage, name='zoomimage'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('guide', views.guide, name='guide'),
    path('photoupload', views.photoupload, name='photoupload'),
    ]