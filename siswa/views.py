from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render

from .models import Siswa

class IndexSiswa(ListView):
    queryset = Siswa.objects.all()
    
def siswa(request):
    queryset = Siswa.objects.all()
    con = {
        'siswa':queryset

    } 
    return render(request, 'pkl/siswa.html', con)

# class list_siswa(CreateView):
#     model = Siswa
#     fields = '__all__'
#     success_url = reverse_lazy('')
