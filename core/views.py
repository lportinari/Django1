from django.shortcuts import render

from .models import Produto
# criando as minhas funções e retornando os meus templates


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django Fromework',
        'outro': 'Django é massa!',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)
