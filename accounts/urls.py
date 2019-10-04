# myblog/accounts/urls.py

from django.urls import path
from . import views #accounts内のviewsをインポートしてくるから、from以降は .　のみになる

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

