from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render

from .models import Perusahaan

class IndexPerusahaan(ListView):
    queryset = Perusahaan.objects.all()
    
def perusahaan(request):
    queryset = Perusahaan.objects.all()
    con = {
        'perusahaan':queryset

    } 
    return render(request, 'pkl/perusahaan.html', con)

# class list_siswa(CreateView):
#     model = Siswa
#     fields = '__all__'
#     success_url = reverse_lazy('')
