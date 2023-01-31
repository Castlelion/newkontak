from django.urls import path, include

from rest_framework import routers
from perusahaan.apiviews import *

router = routers.DefaultRouter()
router.register('perusahaan', PerusahaanViewSet)

from . import views

app_name = 'perusahaan'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.perusahaan, name='perusahaan'),
    # path('', views.IndexSiswa.as_view(), name='index'),
]