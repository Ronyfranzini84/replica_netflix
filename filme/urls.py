from django.urls import path
from . import views
from .views import Homepage, Homefilmes

app_name = 'filme'

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('filmes/', views.Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>/', views.DetalheFilme.as_view(), name='detalhes_filme'),
]