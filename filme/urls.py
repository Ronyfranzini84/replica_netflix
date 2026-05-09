from django.urls import path, reverse_lazy
from . import views
from .views import Homepage, Homefilmes, DetalheFilme, PesquisaFilme, Paginaperfil, CriarConta
from django.contrib.auth import views as auth_views

app_name = 'filme'

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('filmes/', views.Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>/', views.DetalheFilme.as_view(), name='detalhes_filme'),
    path('pesquisa/', views.PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', views.Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', views.CriarConta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]