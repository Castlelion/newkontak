from django.urls import path, include

from rest_framework import routers
from sekolah.apiviews import *

router = routers.DefaultRouter()
router.register('sekolah', SekolahViewSet)
# router.register()


from . import views

app_name = 'sekolah'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.sekolah, name='sekolah'),
]