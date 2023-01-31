from perusahaan.models import Perusahaan
from rest_framework import serializers
# from django.contrib.auth.models import User, Group


class PerusahaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perusahaan
        fields = ['id', 'nama', 'alamat']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
