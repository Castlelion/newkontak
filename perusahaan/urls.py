from django.urls import path

from . import views

app_name = 'perusahaan'

urlpatterns = [
    path('', views.perusahaan, name='perusahaan'),
    # path('', views.IndexSiswa.as_view(), name='index'),
]