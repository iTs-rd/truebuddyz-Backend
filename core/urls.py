from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ICYJWm7rN3nveG2RRYnORLaEw0Y9ae6O/', admin.site.urls),
    path('api/',include('api.urls')),
    path('auth/',obtain_auth_token),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)