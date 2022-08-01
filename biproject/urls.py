from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import awwwapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', awwwapp.views.home, name='home'),
    path('awwwapp/', include('awwwapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
