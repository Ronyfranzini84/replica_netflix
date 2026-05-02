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

	def get(self, request, *args, **kwargs):
		filme = self.get_object()
		filme.visualizacoes += 1
		filme.save()
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(DetalheFilme, self).get_context_data(**kwargs)
		filme_relacionados = Filme.objects.filter(categoria=self.get_object().categoria) # type: ignore
		context['filme_relacionados'] = filme_relacionados
		return context
