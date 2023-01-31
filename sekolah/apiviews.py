from sekolah.models import Sekolah
from sekolah.serializers import SekolahSerializer
from rest_framework import viewsets, permissions


class SekolahViewSet(viewsets.ModelViewSet):
    queryset = Sekolah.objects.all()
    serializer_class = SekolahSerializer
    permission_classes = [permissions.IsAuthenticated]