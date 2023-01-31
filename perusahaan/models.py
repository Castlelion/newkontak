from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class KategoriPerusahaan(models.TextChoices):
        Pemerintahan = 'Pemerintahan', _('Pemerintahan')
        Negeri = 'Negeri', _('Negeri')

class BidangPerusahaan(models.TextChoices):
        PerusahaanEkstraktif = 'Perusahaan Ekstraktif', _('Perusahaan Ekstraktif')
        PerusahaanAgraris = 'Perusahaan Agraris', _('Perusahaan Agraris')
        PerusahaanDagang = 'Perusahaan Dagang', _('Perusahaan Dagang')
        PerusahaanJasa = 'Perusahaan Jasa', _('Perusahaan Jasa')
        PerusahaanIndustri = 'Perusahaan Industri', _('Perusahaan Industri')

class JabatanPerusahaan(models.TextChoices):
        CEO = 'CEO', _('CEO')
        KabagTU = 'Kabag TU', _('Kabag TU')
        
class Perusahaan(models.Model):
    nama = models.CharField(max_length=50)
    kategori = models.CharField(
        max_length=20,
        choices=KategoriPerusahaan.choices,
        default='',
    )
    bidang = models.CharField(
        max_length=50,
        choices=BidangPerusahaan.choices,
        blank=True,
        null=True,
    )
    alamat = models.TextField(default='')
    nama_pic = models.CharField(max_length=254, blank=True, null=True)
    jabatan = models.CharField(
        max_length=10,
        choices=JabatanPerusahaan.choices,
        blank=True,
        null=True,
    )
    no_tlp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    #default
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="perusahaan_created_by", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['-id']
        


# Create your models here.
