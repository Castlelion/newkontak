from sekolah.models import Sekolah
from rest_framework import serializers
# from django.contrib.auth.models import User, Group


class SekolahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sekolah
        fields = ['id', 'Nama', 'Alamat']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
