from django.urls import path

from . import views

app_name = 'sekolah'

urlpatterns = [
    path('', views.sekolah, name='sekolah'),
    # path('', views.IndexSiswa.as_view(), name='index'),
]