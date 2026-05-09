from django.shortcuts import redirect, render, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomePage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

class Homepage(FormView):
	template_name = "homepage.html"
	form_class = FormHomePage

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('filme:homefilmes')
		else:
			return super().get(request, *args, **kwargs)

		
	def get_success_url(self):
		email = self.request.POST.get('email')
		usuario = Usuario.objects.filter(email=email)
		if usuario:
			return reverse('filme:login')
		else:
			return reverse('filme:criarconta')


# def logout_usuario(request):
# 	logout(request)
# 	return redirect('filme:homepage')

class Homefilmes(LoginRequiredMixin, ListView):
	model = Filme
	template_name = "homefilmes.html"

class DetalheFilme(LoginRequiredMixin, DetailView):
	model = Filme
	template_name = "detalhesfilme.html"

	def get(self, request, *args, **kwargs):
		filme = self.get_object()
		filme.visualizacoes += 1
		filme.save()		
		usuario = request.user
		if usuario.is_authenticated:
			usuario.filmes_vistos.add(filme)
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(DetalheFilme, self).get_context_data(**kwargs)
		filme_relacionados = Filme.objects.filter(categoria=self.get_object().categoria) # type: ignore
		context['filme_relacionados'] = filme_relacionados
		return context
	
class PesquisaFilme(LoginRequiredMixin, ListView):
	model = Filme
	template_name = "pesquisa.html"

	def get_queryset(self):
		query = self.request.GET.get('query')
		if query:
			return Filme.objects.filter(titulo__icontains=query)
		else:
			return Filme.objects.none()
		
class Paginaperfil(LoginRequiredMixin, UpdateView):
	template_name = "editarperfil.html"
	model = Usuario
	fields = ['first_name', 'last_name', 'email']

	def get_success_url(self):
		return reverse('filme:homefilmes')


class CriarConta(FormView):
	template_name = "criarconta.html"
	form_class = CriarContaForm

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)
	

	def get_success_url(self):
		return reverse('filme:login')