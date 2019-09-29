from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #削除完了時に遷移するページ
    template_name = 'accounts/signup.html' #表示に使用するテンプレート

class LoginView(generic.CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login') #削除完了時に遷移するページ
    template_name = 'accounts/login.html'#表示に使用するテンプレート


