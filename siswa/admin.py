from django.contrib import admin
from .models import Siswa

# Register your models here.
class namaSiswa(admin.ModelAdmin):
    list_display = ['NISN','Nama','Jenis_Kelamin','Email','Hp','Asal_Sekolah','Alamat','Tempat_Lahir','Tanggal_Lahir']

admin.site.register(Siswa,namaSiswa)