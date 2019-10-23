from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ContactFormView, ContactResultView #0915Dnagoでお問い合わせフォームを作成する

app_name = "foodrescue"

# 基本構成pathの第一引数が、URLの表示になる=アクセスするとこと。第二引数がプログラムがみに行く場所
urlpatterns = [
    path("", views.index, name="index"),
    path('index', views.index, name='index'),
    path('operation', views.operation, name='operation'),
    path("service", views.service, name='service'),
    path('privacy', views.privacy, name='privacy'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
    path('required', views.required, name='required'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('guide', views.guide, name='guide'),
    path('main_share/', views.photoupload, name='main_share'),
    path('map/', views.map, name='map'),
    ]