from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
# from django.contrib.auth.views import
from foodrescue.models import Member

# 1019プロフィール更新
from django.views.generic import UpdateView


class LoginView(AuthLoginView):
    template_name = "accounts/login.html"

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # 新規会員登録完了⇨プロフィール入力へ進む
    # reverse_lazy()はreverse()の遅延評価版で、URLConfがロードされる前にURLの逆引きをしたい時に使う。
    # クラスベース汎用ビューではreverse_lazy()を使う。
    success_url = reverse_lazy('foodrescue:create_profile')
    # 表示に使用するテンプレート
    template_name = 'accounts/signup.html'


class LogoutView(AuthLogoutView):
    template_name = 'accounts/logout.html'

# 1019プロフィール変更
class UserUpdateView(UpdateView):
    model = Member
    fields = ('name', 'gender', 'age', 'address1', 'self_introduction' )
    # テンプレートファイル名を指定
    template_name = 'accounts/user_form.html'
    # 正常に処理が完了した際のリダイレクト先
    success_url = reverse_lazy('foodrescue:myprofile')
    def get_object(self):
        return self.request.user