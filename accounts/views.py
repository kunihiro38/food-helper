from django.shortcuts import render, redirect, reverse
#1030　reverse追加 updateviewの為
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView

# signupviewに関して。新規登録後⇨即プロフィール登録用
from django.contrib.auth import authenticate, login

# from django.contrib.auth.views import
from foodrescue.models import Member

# 1019プロフィール更新
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

# login_required
from django.contrib.auth.decorators import login_required


class LoginView(AuthLoginView):
    template_name = "accounts/login.html"

class SignUpView(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    def form_valid(self, form):
        form.save()
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        #　signup有効なら下記登録画面へ遷移
        return redirect('foodrescue:create_profile')

class LogoutView(AuthLogoutView):
    template_name = 'accounts/logout.html'
