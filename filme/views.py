from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

class Homepage(TemplateView):
	template_name = "homepage.html"

class Homefilmes(ListView):
	model = Filme
	template_name = "homefilmes.html"

class DetalheFilme(DetailView):
	model = Filme
	template_name = "detalhesfilme.html"
