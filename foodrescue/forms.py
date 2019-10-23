
#coding:utf-8
# フォームは、1.ユーザーの入力データを保持。2.入力データのバリデーション（妥当性チェック）を行い、妥当性検証済みのデータやエラーメッセージを保持する
# classに記載した内容が、html表示時に反映される!!

from django import forms
from .models import Member

# お問い合わせフォーム専用
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class PhotoForm(forms.Form):
    STORE_CHOICES = (
    (1, 'マルエツ調布店'),
    (2, '西友調布店'),
    (3, 'オーケー調布店'),
    (4, '成城石井　トリエ京王調布店'),
    (5, '北野エース調布　パルコ店'),
    )
    store_id = forms.ChoiceField(
    label='店舗',
    widget=forms.Select,
    choices=STORE_CHOICES,
    required=True,
    )
    #　投稿画像
    image = forms.ImageField()

# class FoodrescueForm(forms.ModelForm): # modelformだと簡単だが応用が効きにくい
class FoodrescueForm(forms.Form):
#     class Meta: クラスメタとは
# 参考 https://qiita.com/peijipe/items/009fc487505dfdb03a8d
    model = Member
    name = forms.CharField(
        label="名前",
        max_length=20,
        required=False,
        help_text='※任意'
        )
    #　auth_Userは変更不可にする
    # auth_User
    GENDER_CHOICES = (
    (1, '男'),
    (2, '女'),
    (3, 'その他'),
    )
    gender = forms.ChoiceField(
        label='性別',
        widget=forms.Select,
        choices=GENDER_CHOICES,
        required=True,
        )

    YEAR_CHOICES = (
        (10, '10代'),
        (20, '20代'),
        (30, '30代'),
        (40, '40代'),
        (50, '50代'),
        (60, '60代'),
        (70, '70代'),
        (80, '80代'),
        (90, '90代'),
        )
    age = forms.ChoiceField(
    label='年齢',
    widget=forms.Select,
    choices=YEAR_CHOICES,
    required=True,
    )
    ADDRESS_CHOICES = (
    (1, "北海道"), (2,"青森県"), (3,"岩手県"),(4,"宮城県") ,(5,"秋田県"), (6,"山形県"), (7,"福島県"), (8,"茨城県"), (9,"栃木県"),
    (10,"群馬県"), (11,"埼玉県"), (12,"千葉県"), (13,"東京都"), (14,"神奈川県"), (15,"新潟県"), (16,"富山県"), (17,"石川県"),
    (18,"福井県"), (19,"山梨県"), (20,"長野県"), (21,"岐阜県"), (22,"静岡県"), (23,"愛知県"), (24,"三重県"), (25,"滋賀県"),
    (26,"京都府"), (27,"大阪府"), (28,"兵庫県"), (29,"奈良県"), (30,"和歌山県"), (31,"鳥取県"), (32,"島根県"), (33,"岡山県"),
    (34,"広島県"), (35,"山口県"), (36,"徳島県"), (37,"香川県"), (38,"愛媛県"), (39,"高知県"), (40,"福岡県"), (41,"佐賀県"),
    (42,"長崎県"), (43,"熊本県"), (44,"大分県"), (45,"宮崎県"), (46,"鹿児島県"), (47,"沖縄県")
    )
    address1 = forms.ChoiceField(
        label="都道府県",
        widget=forms.Select,
        choices=ADDRESS_CHOICES,
        required=True,
        )

    self_introduction = forms.CharField(
    label="自己紹介",
    widget=forms.Textarea,
    max_length=200,
    required=False,
#     help_text='※任意'
    )

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
        # cleaned_data　でフォームデータを取得
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")


