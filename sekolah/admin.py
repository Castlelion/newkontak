from django.contrib import admin
from .models import Sekolah     

# Register your models here.
class SekolahAdmin(admin.ModelAdmin):
    list_display = ['NPSN','Nama','Email','Telp','Alamat','Provinsi','Kabupaten_Kota','Kecamatan','Status']

admin.site.register(Sekolah, SekolahAdmin)