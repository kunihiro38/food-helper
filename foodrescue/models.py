# coding:utf-8
# modelはデータベースのテーブルとカラムの定義と、「モデル」と呼ばれるクラスとそのクラス属性の定義を対応させ、DBのレコード1件1件をモデルクラスのオブジェクトとして扱えるようにする仕組み。
from django.db import models
from django.utils import timezone
from datetime import datetime
# class Photo　の store_id専用
from django.core.validators import MaxValueValidator, MinValueValidator


class Member(models.Model):
    """会員モデル"""
    # class Meta:　紐付けるmodelクラスを指定する→今回は使用しない
    """テーブル名を定義"""
    db_table = 'profile'
    # 主キー(id)は自動生成されるので明示的に定義する必要なし
    name = models.CharField(max_length=20)
    # email = models.EmailField(label=('メールアドレス'), required=True, help_text=("Required."))
    auth_User = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    age = models.CharField(max_length=4)
    address1 = models.CharField(max_length=6)
    self_introduction = models.CharField(max_length=200)
    # seeder プルダウンセレクト予定?
    favorite_store1 = models.CharField(verbose_name='お気に入り店舗1', max_length=200, null=True)
    # seeder　プルダウンセレクト予定?
    favorite_store2 = models.CharField(verbose_name='お気に入り店舗2', max_length=200, null=True)
    # seeder プルダウンセレクト予定?
    favorite_store3 = models.CharField(verbose_name='お気に入り店舗3', max_length=200, null=True)
    # 修正必要 参加日時
    created_at = models.DateTimeField(verbose_name='登録日時', default=datetime.now())
    # 修正必要 更新日時
    updated_at = models.DateTimeField(verbose_name='更新日時', default=timezone.now)
    # 修正必要 最終ログイン
    last_login = models.DateTimeField(verbose_name='最終ログイン', default=timezone.now)

    def __str__(self):
        return self.name

# main画面の画像投稿機能
class Photo(models.Model):
    # blank　と　null に関しては、何も記載をしないと両方False登録になる。この場合、投稿時にフィールドの入力は必須で、
    # データベースに保存される値も空になってはいけない。
    # 店舗ID 合計5店舗　name と紐づく1.マルエツ 2.西友 3.オーケー 4.成城石井 5.北野エース
    store_id = models.IntegerField(verbose_name='店舗名',
                                    validators=[MinValueValidator(1),
                                                 MaxValueValidator(5)],
                                     blank=False, null=False,)
    image = models.ImageField(upload_to='images/', verbose_name='画像',)

# 1018店舗登録
class Store(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    bussiness_hours = models.CharField('営業時間', max_length=10)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    # 1023修正
    def get_map_data(self):
        return self.name, self.address, self.lat, self.lng