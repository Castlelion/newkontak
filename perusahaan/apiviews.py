from perusahaan.models import Perusahaan
from perusahaan.serializers import PerusahaanSerializer
from rest_framework import viewsets, permissions


class PerusahaanViewSet(viewsets.ModelViewSet):
    queryset = Perusahaan.objects.all()
    serializer_class = PerusahaanSerializer
    permission_classes = [permissions.IsAuthenticated]