from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from socialproject.settings import MEDIA_ROOT, MEDIA_URL
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/',include('users.urls')),
    path('posts/', include('posts.urls')),
    path('',views.index, name='index')

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)