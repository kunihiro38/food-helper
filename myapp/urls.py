from django.contrib import admin
from django.urls import include, path
# 1004以下を新しく定義
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include('foodrescue.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    ]

# path('web/', include('django.contrib.auth.urls')), ＃これいる？

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

