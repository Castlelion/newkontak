from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.utils.text import slugify

class JenisKelamin(models.TextChoices):
    LAKILAKI ='L', _('Laki-laki')
    PEREMPUAN ='P', _('Perempuan')

# Create your models here.
class Siswa(models.Model):
    NISN = models.CharField(max_length=20)
    Nama = models.CharField(max_length=50)
    Jenis_Kelamin = models.CharField(
        max_length=2,
        choices=JenisKelamin.choices,
    )
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Hp = models.CharField(max_length=15, blank=True, null=True)
    Asal_Sekolah = models.ForeignKey('sekolah.Sekolah', on_delete=models.CASCADE, null=True, blank=True)
    Alamat = models.TextField(blank=True, null=True)

    Tempat_Lahir = models.CharField(max_length=100)
    Tanggal_Lahir = models.DateField(blank=True ,null=True)

    # default
    # create_by =
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nama

    # def save (self, *args, **kwargs):
    #     self.slug = slugify(self.Nama)
    #     super(Siswa, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

        