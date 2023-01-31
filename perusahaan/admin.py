from django.contrib import admin
from .models import Perusahaan

# Register your models here.
class dataPerusahaan(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'bidang', 'alamat', 'nama_pic', 'jabatan', 'no_tlp', 'email', 'created_by', 'created_at', 'updated_at' ]

admin.site.register(Perusahaan, dataPerusahaan)