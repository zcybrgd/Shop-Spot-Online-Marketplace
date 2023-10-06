import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from core.views import contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('items.urls')),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('__debug__/', include(debug_toolbar.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

