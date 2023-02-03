from django.contrib import admin
from django.urls import path, include

from guitarworld.views import pageNotFound 
from mysite import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guitarworld.urls')),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
