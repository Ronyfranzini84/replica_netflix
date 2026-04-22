from django.urls import path
from . import views
from .views import homepage

urlpatterns = [
    path('', views.homepage, name='index'),
    # suas outras rotas aqui...
]