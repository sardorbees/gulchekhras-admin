from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from media_app.views import MediaItemViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'media-items', MediaItemViewSet, basename='mediaitem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# serve media in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
