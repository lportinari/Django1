from django.urls import path

# Chamei as funções index e contato do meu arquivo views
from .views import index, contato

# criei minha lista urlpatterns como no arquivo urls do projeto e adicionei os meus paths
urlpatterns = [
    path('', index),
    path('contato', contato),
]