#coding:utf-8
# modelはデータベースのテーブルとカラムの定義と、「モデル」と呼ばれるクラスとそのクラス属性の定義を対応させ、DBのレコード1件1件をモデルクラスのオブジェクトとして扱えるようにする仕組み。
from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Member(models.Model):
    """会員モデル"""
    class Meta:
        """テーブル名を定義"""
        db_table = 'profile'
    # テーブルのカラムに対応するフィールドを定義
    # 主キー(id)は自動生成されるので明示的に定義する必要なし
    # null制約（デフォルト値はFalse:許可しない)
    name = models.CharField(verbose_name='名前', max_length=20)
    #本来的には、新規会員登録した際のメールアドレスをここに使用したい
    #⇨signupから直接プロフィール作成画面に飛ばすから、メールアドレスは既に登録されたものとして扱うので、ここでは作成しない
    #email = models.EmailField(label=('メールアドレス'), required=True, help_text=("Required."))
    # 本来的には、新規会員登録した際のメールアドレスをここに使用したい　
    """
     →　ここはauth_userとの結合をすればいいのではないでしょうか？
      help_text=_("Required.")でmigrationsを実行するとエラーになります。対応願います。

    """
    email = models.EmailField(label=('メールアドレス'), required=True, help_text=("Required."))
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女'),
        (3, 'その他'),
        )
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    # 年齢のプルダウン参考　https://qiita.com/okoppe8/items/a1149b2be54441951de1
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
    age = models.IntegerField(verbose_name='年齢', choices=YEAR_CHOICES)
    # 住所は市町村まで　※参考　https://qiita.com/kk-ster/items/4618dd0a499c2c405b47
    """
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/#blank
    住所はバリデーションでnullを許容して、DBはnullを許容しない？

    """
    zip_code = models.CharField(
        verbose_name='郵便番号', max_length=8, blank=True,
        )
    address1 = models.CharField(
        verbose_name='都道府県', max_length=40, blank=True,
        )
    address2 = models.CharField(
        verbose_name='市区町村番地', max_length=40, blank=True,
        )
    # 自己紹介
    """
    自己紹介は本当にChar型の200長で大丈夫？

    """
    self_introduction = models.CharField(verbose_name='自己紹介', max_length=200, null=True)
    # お気に入り店舗1 プルダウンセレクトしたい
    """
    このようにデータを持たせると、店舗名が変わったときや閉店になったときなどに苦労しない？大丈夫？

    """
    favorite_store1 = models.CharField(verbose_name='お気に入り店舗1', max_length=200, null=True)
    # お気に入り店舗2　プルダウンセレクトしたい
    favorite_store2 = models.CharField(verbose_name='お気に入り店舗2', max_length=200, null=True)
    # お気に入り店舗1 プルダウンセレクトしたい
    favorite_store3 = models.CharField(verbose_name='お気に入り店舗3', max_length=200, null=True)
    #参加日時
    created_at = models.DateTimeField(verbose_name='登録日時', default=datetime.now())
    #更新日時
    updated_at = models.DateTimeField(verbose_name='更新日時', default=timezone.now)
    #最終ログイン
    last_login = models.DateTimeField(verbose_name='最終ログイン', default=timezone.now)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

#     def __str__(self): #これがないとmigrateした時にデータベースが作成されない!!!⇨0914いや、全く関係なかったこれ。
#         return '&lt;User:id =' + str(self.id) + self.username + ')&gt;'


#     def __str__(self): #これがないとmigrateした時にデータベースが作成されない!!!
#         return '&lt;Friend:id =' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')&gt;'
#     &lt;や&gt;はタグなどに使われる開始（<）終了（>)タグを意味する。