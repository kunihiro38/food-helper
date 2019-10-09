#coding:utf-8
# フォームは、1.ユーザーの入力データを保持。2.入力データのバリデーション（妥当性チェック）を行い、妥当性検証済みのデータやエラーメッセージを保持する
# classに記載した内容が、html表示時に反映される!!

from django import forms
from .models import Member
from foodrescue.models import Member

# お問い合わせフォーム専用
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class FoodrescueForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'gender', 'age', 'zip_code', 'address1', 'address2', 'self_introduction',
                  'favorite_store1', 'favorite_store2', 'favorite_store3', 'created_at', 'updated_at', 'last_login']



# お問い合わせフォーム作成#
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
