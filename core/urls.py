from django.urls import path

# Chamei as funções index e contato do meu arquivo views
from .views import index, contato, produto

# criei minha lista urlpatterns como no arquivo urls do projeto e adicionei os meus paths
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]