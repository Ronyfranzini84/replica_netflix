from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    # suas outras rotas aqui...
]