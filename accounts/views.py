from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView

class LoginView(AuthLoginView):
    template_name = "accounts/login.html"

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #削除完了時に遷移するページ
    template_name = 'accounts/signup.html' #表示に使用するテンプレート

class LogoutView(AuthLogoutView):
    template_name = "accounts/logout.html"