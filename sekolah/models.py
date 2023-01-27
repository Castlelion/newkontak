from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class StatusSekolah(models.TextChoices):
    SWASTA ='Swasta', _('Swasta')
    NEGERI ='Negeri', _('Negeri')


class Sekolah(models.Model):
    NPSN = models.CharField(max_length=10, default='')
    Nama = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Telp = models.CharField(max_length=13, blank=True, null=True)
    Alamat = models.TextField(blank=True, null=True)
    Provinsi = models.CharField(blank=True, null=True, max_length=50)
    Kabupaten_Kota = models.CharField(blank=True, null=True, max_length=50)
    Kecamatan =  models.CharField(blank=True, null=True, max_length=50)
    Status = models.CharField(
        max_length=10,
        choices=StatusSekolah.choices,
        null=False,
        default='0'
    )
    # default
    create_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="sekolah_created_by")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nama

    class Meta:
        db_table = "Sekolah"
        ordering = ['-id']
        verbose_name_plural = "Sekolah"
        


# Create your models here.
