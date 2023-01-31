from siswa.models import Siswa
from rest_framework import serializers


class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = ['id', 'Nama', 'Alamat']
