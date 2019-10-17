from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    bussiness_hours = models.CharField('営業時間', max_length=10)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "店名"
        verbose_name_plural = '店名'