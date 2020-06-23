from django.shortcuts import render
from django.http import Http404 
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Artikel 

class ArtikelListView(ListView):
	model = Artikel 
	context_object_name = 'artikel_list'
	template_name = 'artikel/home_artikel.html'
	ordering = ['-published']
	paginate_by = 3

class ArtikelDetailView(DetailView):
	model = Artikel 
	context_object_name = 'artikel'
	template_name = 'artikel/detail.html'



