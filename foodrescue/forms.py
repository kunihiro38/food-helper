#coding:utf-8
# フォームは、1.ユーザーの入力データを保持。2.入力データのバリデーション（妥当性チェック）を行い、妥当性検証済みのデータやエラーメッセージを保持する
# classに記載した内容が、html表示時に反映される!!

from django import forms
from .models import User
# from foodrescue.models import User #0911追加これ入力したらなぜか行けた・・・0917 foodrescueを追記
from django.contrib.auth.forms import UserCreationForm #0911追加

# 0915お問い合わせフォーム作成#
from django.conf import settings
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponse
# 0915お問い合わせフォーム作成#

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        class Meta:#class Metaとは・・・「class文の持つ定義する機能」を定義する機能
            model = User
            fields = ("username","password1","password2",) #0911 ()だとまた何か違うのか？⇨どっちも一緒

# なぜかここのMetaタグを上のdefに合わせると上手く表示される・・・なぜ？？？？？


# 0915お問い合わせフォーム作成#
class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
