from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render

from .models import Sekolah

class IndexSekolah(ListView):
    queryset = Sekolah.objects.all()
    
def sekolah(request):
    queryset = Sekolah.objects.all()
    con = {
        'sekolah':queryset

    } 
    return render(request, 'pkl/sekolah.html', con)