from siswa.models import Siswa
from siswa.serializers import SiswaSerializer
from rest_framework import viewsets, permissions


class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    permission_classes = [permissions.IsAuthenticated]