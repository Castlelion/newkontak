from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    # path('', include('home.urls')),
    # path("", include('admin_berry.urls')),
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('siswa/', include('siswa.urls')),
    path('perusahaan/', include('perusahaan.urls')),
    path('sekolah/', include('sekolah.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
