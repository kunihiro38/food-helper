
from django.contrib import admin
from django.urls import include, path
# 1004以下を新しく定義
from django.conf import settings
from django.conf.urls.static import static
# 1016 GoogleMap専用
from foodrescue.models import Store

from rest_framework import routers, serializers, viewsets

from accounts import views as accounts_views



# 1016　GoogleMAP専用
# モデルをJSONにマッピング（変換）するシリアライザ
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'address', 'bussiness_hours', 'lat', 'lng')

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# 参考 https://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter()
# register 引数2つ(prefix & the viewset class
router.register(r'store', StoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include('foodrescue.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('gmap/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ]

# 1018 path(gmap/api/ ⇨　django　の仕組み上第一引数のURLにアクセス時に、第二引数へ飛ぶ
# 1018 path(api-auth) ⇨　gmap表示状のスーパーの登録・管理サイト

# path('web/', include('django.contrib.auth.urls')), ＃これいる？
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
