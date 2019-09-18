#coding:utf-8
# modelはデータベースのテーブルとカラムの定義と、「モデル」と呼ばれるクラスとそのクラス属性の定義を対応させ、DBのレコード1件1件をモデルクラスのオブジェクトとして扱えるようにする仕組み。

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

#     def __str__(self): #これがないとmigrateした時にデータベースが作成されない!!!⇨0914いや、全く関係なかったこれ。
#         return '&lt;User:id =' + str(self.id) + self.username + ')&gt;'

# class Friend(models.Model):
#     class Meta:
        #テーブル名を定義
#         db_table = "sample"
#     name = models.CharField(max_length=100)
#     mail = models.EmailField(max_length=200)
#     age = models.IntegerField(default=0)

#     def __str__(self): #これがないとmigrateした時にデータベースが作成されない!!!
#         return '&lt;Friend:id =' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')&gt;'
#     &lt;や&gt;はタグなどに使われる開始（<）終了（>)タグを意味する。


