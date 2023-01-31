from django.urls import path, include

from rest_framework import routers
from siswa.apiviews import *

router = routers.DefaultRouter()
router.register('siswa', SiswaViewSet)

from . import views

app_name = 'siswa'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.siswa, name='siswa'),
    # path('', views.IndexSiswa.as_view(), name='index'),
]